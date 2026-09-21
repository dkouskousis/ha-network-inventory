"""Persistent inventory storage."""

from __future__ import annotations

import asyncio
from copy import deepcopy
from datetime import UTC, datetime
from typing import Any
from uuid import uuid4

from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store

from .const import (
    DEFAULT_DEVICE_TYPES,
    DEFAULT_PROTOCOLS,
    DEVICE_TYPES_VERSION,
    IP_PROTOCOLS,
    STORAGE_KEY,
    STORAGE_VERSION,
)


class InventoryError(ValueError):
    """Raised when inventory data is invalid."""


def common_entity_name(entity_ids: list[str]) -> str:
    """Return the common name shared by a device's entity IDs."""
    names = [entity_id.partition(".")[2].split("_") for entity_id in entity_ids]
    if not names:
        return ""
    common: list[str] = []
    for index, part in enumerate(names[0]):
        if all(len(name) > index and name[index] == part for name in names[1:]):
            common.append(part)
        else:
            break
    return "_".join(common)


class InventoryStore:
    """Manage the inventory and its monotonically increasing IDs."""

    def __init__(self, hass: HomeAssistant) -> None:
        self._store: Store[dict[str, Any]] = Store(
            hass, STORAGE_VERSION, STORAGE_KEY, private=True, atomic_writes=True
        )
        self._lock = asyncio.Lock()
        self.data: dict[str, Any] = {}

    async def async_load(self) -> None:
        """Load data and add defaults for new installations."""
        loaded = await self._store.async_load()
        migrated = False
        self.data = loaded or {
            "devices": [],
            "protocols": deepcopy(DEFAULT_PROTOCOLS),
            "device_types": list(DEFAULT_DEVICE_TYPES),
            "device_types_version": DEVICE_TYPES_VERSION,
            "brands": [],
            "counters": {
                key: value["start"] - 1 for key, value in DEFAULT_PROTOCOLS.items()
            },
        }
        self.data.setdefault("devices", [])
        self.data.setdefault("protocols", deepcopy(DEFAULT_PROTOCOLS))
        self.data.setdefault("device_types", list(DEFAULT_DEVICE_TYPES))
        if self.data.get("device_types_version", 0) < DEVICE_TYPES_VERSION:
            current_types = {item.casefold() for item in self.data["device_types"]}
            self.data["device_types"].extend(
                item
                for item in DEFAULT_DEVICE_TYPES
                if item.casefold() not in current_types
            )
            self.data["device_types_version"] = DEVICE_TYPES_VERSION
            migrated = True
        self.data.setdefault(
            "brands",
            sorted(
                {
                    str(device.get("brand", "")).strip()
                    for device in self.data["devices"]
                    if str(device.get("brand", "")).strip()
                },
                key=str.casefold,
            ),
        )
        self.data.setdefault("counters", {})
        for key, value in self.data["protocols"].items():
            self.data["counters"].setdefault(key, value["start"] - 1)
        if migrated:
            await self._store.async_save(self.data)

    async def async_snapshot(self) -> dict[str, Any]:
        """Return a safe copy of all stored data."""
        return deepcopy(self.data)

    async def async_add(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Create a device and assign its permanent device code."""
        async with self._lock:
            device = self._clean_device(payload)
            protocol = device["protocol"]
            device_code = self._next_device_code(protocol)
            now = _now()
            device.update(
                {
                    "id": uuid4().hex,
                    "device_code": device_code,
                    "protocol": protocol,
                    "created_at": now,
                    "updated_at": now,
                }
            )
            self.data["devices"].append(device)
            self._remember_brand(device["brand"])
            await self._store.async_save(self.data)
            return deepcopy(device)

    async def async_update(
        self, internal_id: str, payload: dict[str, Any]
    ) -> dict[str, Any]:
        """Update a device without changing its permanent device code."""
        async with self._lock:
            device = self._find(internal_id)
            reset_device_code = (
                "device_code" in payload and payload.get("device_code") in (None, "")
            )
            updated = self._clean_device({**device, **payload})
            protected = {
                "id": device["id"],
                "device_code": (
                    self._next_device_code(updated["protocol"])
                    if reset_device_code
                    else device["device_code"]
                ),
                "created_at": device["created_at"],
            }
            device.clear()
            device.update(updated)
            device.update(protected)
            device["protocol"] = self._normalise_protocol(device.get("protocol"))
            device["updated_at"] = _now()
            self._remember_brand(device["brand"])
            await self._store.async_save(self.data)
            return deepcopy(device)

    async def async_delete(self, internal_id: str) -> None:
        """Delete a device. Its numeric code remains consumed."""
        async with self._lock:
            device = self._find(internal_id)
            self.data["devices"].remove(device)
            await self._store.async_save(self.data)

    async def async_import(self, rows: list[dict[str, Any]]) -> dict[str, int]:
        """Import rows, preserving valid unique codes when supplied."""
        async with self._lock:
            imported = 0
            skipped = 0
            existing_codes = {
                int(device["device_code"]) for device in self.data["devices"]
            }
            existing_ha_ids = {
                device.get("ha_device_id")
                for device in self.data["devices"]
                if device.get("ha_device_id")
            }

            for payload in rows:
                if payload.get("ha_device_id") in existing_ha_ids:
                    skipped += 1
                    continue
                device = self._clean_device(payload)
                protocol = device["protocol"]
                supplied_code = _to_int(payload.get("device_code"))
                if supplied_code is not None:
                    config = self.data["protocols"][protocol]
                    if not config["start"] <= supplied_code <= config["end"]:
                        raise InventoryError(
                            f"Device code {supplied_code} is outside the {config['label']} range"
                        )
                    if supplied_code in existing_codes:
                        raise InventoryError(f"Device code {supplied_code} already exists")
                    device_code = supplied_code
                    self.data["counters"][protocol] = max(
                        self.data["counters"].get(protocol, config["start"] - 1),
                        supplied_code,
                    )
                else:
                    device_code = self._next_device_code(protocol)

                now = _now()
                device.update(
                    {
                        "id": uuid4().hex,
                        "device_code": device_code,
                        "protocol": protocol,
                        "created_at": now,
                        "updated_at": now,
                    }
                )
                self.data["devices"].append(device)
                self._remember_brand(device["brand"])
                existing_codes.add(device_code)
                if device.get("ha_device_id"):
                    existing_ha_ids.add(device["ha_device_id"])
                imported += 1

            await self._store.async_save(self.data)
            return {"imported": imported, "skipped": skipped}

    async def async_save_settings(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Save protocol ranges, device types, and brands."""
        async with self._lock:
            protocols = payload.get("protocols", self.data["protocols"])
            cleaned: dict[str, dict[str, Any]] = {}
            ranges: list[tuple[int, int, str]] = []
            for raw_key, value in protocols.items():
                key = _slug(raw_key)
                if not key or key in cleaned:
                    raise InventoryError("Every protocol needs a unique name")
                start = _to_int(value.get("start"))
                end = _to_int(value.get("end"))
                if start is None or end is None or start < 1 or end < start:
                    raise InventoryError(f"Invalid range for {raw_key}")
                for other_start, other_end, other_key in ranges:
                    if start <= other_end and end >= other_start:
                        raise InventoryError(
                            f"The ranges for {raw_key} and {other_key} overlap"
                        )
                ranges.append((start, end, key))
                cleaned[key] = {
                    "label": str(value.get("label") or raw_key).strip()[:60],
                    "start": start,
                    "end": end,
                    "color": str(value.get("color") or "#64748b")[:20],
                }

            used_protocols = {device["protocol"] for device in self.data["devices"]}
            if missing := used_protocols - cleaned.keys():
                raise InventoryError(
                    "Protocols used by devices cannot be removed: " + ", ".join(missing)
                )
            for device in self.data["devices"]:
                config = cleaned[device["protocol"]]
                if not config["start"] <= int(device["device_code"]) <= config["end"]:
                    raise InventoryError(
                        f"Existing device {device['device_code']} is outside the new range"
                    )

            device_types = sorted(
                {
                    str(item).strip()[:80]
                    for item in payload.get("device_types", self.data["device_types"])
                    if str(item).strip()
                },
                key=str.casefold,
            )
            if not device_types:
                raise InventoryError("At least one device type is required")

            brands = {
                str(item).strip()[:100]
                for item in payload.get("brands", self.data["brands"])
                if str(item).strip()
            }
            brands.update(
                device["brand"] for device in self.data["devices"] if device["brand"]
            )

            self.data["protocols"] = cleaned
            self.data["device_types"] = device_types
            self.data["brands"] = sorted(brands, key=str.casefold)
            for key, config in cleaned.items():
                self.data["counters"].setdefault(key, config["start"] - 1)
            await self._store.async_save(self.data)
            return await self.async_snapshot()

    def _next_device_code(self, protocol: str) -> int:
        config = self.data["protocols"][protocol]
        current = max(
            self.data["counters"].get(protocol, config["start"] - 1),
            config["start"] - 1,
        )
        candidate = current + 1
        if candidate > config["end"]:
            raise InventoryError(f"No device codes remain for {config['label']}")
        self.data["counters"][protocol] = candidate
        return candidate

    def _normalise_protocol(self, value: Any) -> str:
        protocol = _slug(value or "other")
        protocol = {
            "wi_fi": "wifi",
            "wireless": "wifi",
            "zig_bee": "zigbee",
            "ble": "bluetooth",
            "z_wave": "zwave",
            "lan": "ethernet",
            "wired": "ethernet",
        }.get(protocol, protocol)
        if protocol not in self.data["protocols"]:
            raise InventoryError(f"Unknown protocol: {value}")
        return protocol

    def _find(self, internal_id: str) -> dict[str, Any]:
        for device in self.data["devices"]:
            if device["id"] == internal_id:
                return device
        raise InventoryError("Device not found")

    def _remember_brand(self, brand: str) -> None:
        if not any(item.casefold() == brand.casefold() for item in self.data["brands"]):
            self.data["brands"].append(brand)
            self.data["brands"].sort(key=str.casefold)

    def _clean_device(self, payload: dict[str, Any]) -> dict[str, Any]:
        allowed = (
            "name",
            "device_type",
            "brand",
            "model",
            "area",
            "mac",
            "ip_address",
            "protocol",
            "device_identifier",
            "entity_name",
            "comments",
            "status",
            "ha_device_id",
            "integration",
        )
        cleaned = {
            key: str(payload.get(key, "") or "").strip()[:1000] for key in allowed
        }
        for brand in self.data["brands"]:
            if brand.casefold() == cleaned["brand"].casefold():
                cleaned["brand"] = brand
                break
        if cleaned["protocol"]:
            cleaned["protocol"] = self._normalise_protocol(cleaned["protocol"])
        required = {
            "name": "Device name",
            "device_type": "Type",
            "brand": "Brand",
            "area": "Area",
            "protocol": "Protocol",
            "mac": "MAC / IEEE",
        }
        missing = [label for key, label in required.items() if not cleaned[key]]
        if cleaned["protocol"] in IP_PROTOCOLS and not cleaned["ip_address"]:
            missing.append("IP address")
        if missing:
            raise InventoryError("Required fields: " + ", ".join(missing))
        cleaned["status"] = cleaned["status"] or "unknown"
        return cleaned


def _slug(value: Any) -> str:
    return (
        str(value)
        .strip()
        .lower()
        .replace("-", "_")
        .replace(" ", "_")[:40]
    )


def _to_int(value: Any) -> int | None:
    if value in (None, ""):
        return None
    try:
        return int(value)
    except (TypeError, ValueError):
        return None


def _now() -> str:
    return datetime.now(UTC).isoformat()
