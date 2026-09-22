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
    DEFAULT_TAGS,
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
            "tags": list(DEFAULT_TAGS),
            "logs": [],
            "backups": [],
            "counters": {
                key: value["start"] - 1 for key, value in DEFAULT_PROTOCOLS.items()
            },
        }
        self.data.setdefault("devices", [])
        self.data.setdefault("protocols", deepcopy(DEFAULT_PROTOCOLS))
        self.data.setdefault("device_types", list(DEFAULT_DEVICE_TYPES))
        self.data.setdefault("tags", list(DEFAULT_TAGS))
        self.data.setdefault("logs", [])
        self.data.setdefault("backups", [])
        if len(self.data["logs"]) > 500:
            self.data["logs"] = self.data["logs"][-500:]
            migrated = True
        self.data.setdefault(
            "niimbot",
            {"device_id": "", "label_width_mm": 30, "label_height_mm": 15, "margin_mm": 1.5, "top_margin_mm": 2},
        )
        self.data["niimbot"].setdefault("label_width_mm", 30)
        self.data["niimbot"].setdefault("label_height_mm", 15)
        self.data["niimbot"].setdefault("margin_mm", 1.5)
        self.data["niimbot"].setdefault("top_margin_mm", 2)
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
        for device in self.data["devices"]:
            device.setdefault("network", "")
            device.setdefault("vlan", "")
            device.setdefault("ssid", "")
            device.setdefault("connected_device", "")
            device.setdefault("switch_port", "")
            device.setdefault("tags", [])
            device.setdefault("battery_entity_id", "")
            device.setdefault("battery_last_replaced_at", "")
            device.setdefault("battery_history", [])
            device.setdefault("primary_entity_id", "")
        if migrated:
            await self._store.async_save(self.data)

    async def async_snapshot(self) -> dict[str, Any]:
        """Return a safe copy of all stored data."""
        result = deepcopy(self.data)
        result["backups"] = [
            {key: value for key, value in backup.items() if key != "data"}
            for backup in result.get("backups", [])
        ]
        return result

    async def async_export(self) -> dict[str, Any]:
        """Return a portable JSON backup."""
        return {
            "schema": "network_inventory_backup",
            "version": 1,
            "exported_at": _now(),
            "data": self._backup_data(),
        }

    async def async_restore(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Restore a JSON export after preserving the current state."""
        async with self._lock:
            incoming = payload.get("data") if payload.get("schema") == "network_inventory_backup" else payload
            if not isinstance(incoming, dict):
                raise InventoryError("Invalid Network Inventory backup")
            restored = self._validate_restore(incoming)
            self._create_backup("before_restore")
            backups = self.data["backups"]
            self.data = restored
            self.data["backups"] = backups
            self._record_log("restore", details="JSON backup restored", source="restore")
            await self._store.async_save(self.data)
            return await self.async_snapshot()

    async def async_restore_backup(self, backup_id: str) -> dict[str, Any]:
        """Restore one automatically-created internal backup."""
        async with self._lock:
            backup = next(
                (item for item in self.data["backups"] if item["id"] == backup_id),
                None,
            )
            if backup is None:
                raise InventoryError("Backup not found")
            target_data = deepcopy(backup["data"])
            restored = self._validate_restore(target_data)
            self._create_backup("before_restore")
            backups = self.data["backups"]
            self.data = restored
            self.data["backups"] = backups
            self._record_log(
                "restore", details=f"Automatic backup restored: {backup['created_at']}", source="backup"
            )
            await self._store.async_save(self.data)
            return await self.async_snapshot()

    async def async_save_niimbot(
        self,
        device_id: str,
        label_width_mm: float,
        label_height_mm: float,
        margin_mm: float,
        top_margin_mm: float,
    ) -> dict[str, Any]:
        """Save the Home Assistant device used for label printing."""
        async with self._lock:
            self.data["niimbot"] = {
                "device_id": str(device_id).strip(),
                "label_width_mm": label_width_mm,
                "label_height_mm": label_height_mm,
                "margin_mm": margin_mm,
                "top_margin_mm": top_margin_mm,
            }
            await self._store.async_save(self.data)
            return deepcopy(self.data["niimbot"])

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
            self._append_initial_battery_history(device)
            self.data["devices"].append(device)
            self._remember_brand(device["brand"])
            self._remember_tags(device["tags"])
            self._record_log("add", device=device, changes=self._device_changes({}, device))
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
            previous = deepcopy(device)
            if (
                updated["battery_last_replaced_at"]
                and updated["battery_last_replaced_at"]
                != previous.get("battery_last_replaced_at", "")
            ):
                updated["battery_history"].append(
                    self._battery_history_entry(updated["battery_last_replaced_at"])
                )
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
            self._remember_tags(device["tags"])
            changes = self._device_changes(previous, device)
            if changes:
                self._record_log("update", device=device, changes=changes)
            await self._store.async_save(self.data)
            return deepcopy(device)

    async def async_record_battery_replacement(
        self, internal_id: str, replaced_at: str, note: str = ""
    ) -> dict[str, Any]:
        """Record a battery replacement in the device's permanent history."""
        async with self._lock:
            device = self._find(internal_id)
            replacement = self._battery_history_entry(replaced_at, note)
            device.setdefault("battery_history", []).append(replacement)
            device["battery_last_replaced_at"] = replacement["replaced_at"]
            device["updated_at"] = _now()
            self._record_log(
                "battery_replaced",
                device=device,
                details=f"Battery replaced on {replacement['replaced_at']}",
                source="battery",
            )
            await self._store.async_save(self.data)
            return deepcopy(device)

    async def async_bulk_update(
        self,
        device_ids: list[str],
        fields: dict[str, Any],
        tag_mode: str = "",
        tags: list[str] | None = None,
    ) -> dict[str, Any]:
        """Update selected fields on multiple devices as one operation."""
        allowed_fields = {
            "device_type",
            "brand",
            "network",
            "vlan",
            "ssid",
            "connected_device",
            "switch_port",
        }
        unknown = set(fields) - allowed_fields
        if unknown:
            raise InventoryError("Unsupported bulk fields: " + ", ".join(sorted(unknown)))
        if tag_mode not in {"", "add", "remove", "replace"}:
            raise InventoryError("Invalid bulk tag operation")
        if not fields and not tag_mode:
            raise InventoryError("Select at least one field to update")

        unique_ids = list(dict.fromkeys(str(item) for item in device_ids if str(item)))
        if not unique_ids:
            raise InventoryError("Select at least one device")

        async with self._lock:
            devices = [self._find(internal_id) for internal_id in unique_ids]
            original = deepcopy(self.data)
            backup_id = self._create_backup("before_bulk_update")["id"]
            try:
                changed_count = 0
                requested_tags = {
                    str(tag).strip()[:60] for tag in (tags or []) if str(tag).strip()
                }
                for device in devices:
                    payload = {**device, **fields}
                    current_tags = set(device.get("tags", []))
                    if tag_mode == "add":
                        payload["tags"] = sorted(current_tags | requested_tags, key=str.casefold)
                    elif tag_mode == "remove":
                        remove = {tag.casefold() for tag in requested_tags}
                        payload["tags"] = [
                            tag for tag in current_tags if tag.casefold() not in remove
                        ]
                    elif tag_mode == "replace":
                        payload["tags"] = sorted(requested_tags, key=str.casefold)

                    updated = self._clean_device(payload)
                    previous = deepcopy(device)
                    protected = {
                        "id": device["id"],
                        "device_code": device["device_code"],
                        "created_at": device["created_at"],
                    }
                    device.clear()
                    device.update(updated)
                    device.update(protected)
                    changes = self._device_changes(previous, device)
                    if not changes:
                        continue
                    device["updated_at"] = _now()
                    self._remember_brand(device["brand"])
                    self._remember_tags(device["tags"])
                    self._record_log(
                        "bulk_update",
                        device=device,
                        changes=changes,
                        source="bulk",
                    )
                    changed_count += 1
            except InventoryError:
                self.data = original
                raise

            await self._store.async_save(self.data)
            return {
                "selected": len(devices),
                "updated": changed_count,
                "backup_id": backup_id,
            }

    async def async_delete(self, internal_id: str) -> None:
        """Delete a device. Its numeric code remains consumed."""
        async with self._lock:
            device = self._find(internal_id)
            self._record_log("delete", device=device, changes=self._device_changes(device, {}))
            self.data["devices"].remove(device)
            await self._store.async_save(self.data)

    async def async_import(self, rows: list[dict[str, Any]]) -> dict[str, Any]:
        """Import rows, preserving valid unique codes when supplied."""
        async with self._lock:
            backup_id = ""
            if len(rows) > 1:
                backup_id = self._create_backup("before_bulk_import")["id"]
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
            existing_unifi_ids = {
                device.get("unifi_id")
                for device in self.data["devices"]
                if device.get("unifi_id")
            }

            for payload in rows:
                if payload.get("ha_device_id") in existing_ha_ids:
                    skipped += 1
                    continue
                if payload.get("unifi_id") in existing_unifi_ids:
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
                self._append_initial_battery_history(device)
                self.data["devices"].append(device)
                self._remember_brand(device["brand"])
                self._remember_tags(device["tags"])
                self._record_log(
                    "import", device=device, changes=self._device_changes({}, device), source="import"
                )
                existing_codes.add(device_code)
                if device.get("ha_device_id"):
                    existing_ha_ids.add(device["ha_device_id"])
                if device.get("unifi_id"):
                    existing_unifi_ids.add(device["unifi_id"])
                imported += 1

            await self._store.async_save(self.data)
            return {"imported": imported, "skipped": skipped, "backup_id": backup_id}

    async def async_save_settings(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Save protocol ranges, device types, brands, and tags."""
        async with self._lock:
            previous = {
                "protocols": deepcopy(self.data["protocols"]),
                "device_types": deepcopy(self.data["device_types"]),
                "brands": deepcopy(self.data["brands"]),
                "tags": deepcopy(self.data["tags"]),
            }
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

            tags = {
                str(item).strip()[:60]
                for item in payload.get("tags", self.data["tags"])
                if str(item).strip()
            }
            tags.update(tag for device in self.data["devices"] for tag in device.get("tags", []))

            self.data["protocols"] = cleaned
            self.data["device_types"] = device_types
            self.data["brands"] = sorted(brands, key=str.casefold)
            self.data["tags"] = sorted(tags, key=str.casefold)
            for key, config in cleaned.items():
                self.data["counters"].setdefault(key, config["start"] - 1)
            current = {key: deepcopy(self.data[key]) for key in previous}
            changes = self._device_changes(previous, current)
            if changes:
                self._record_log("settings", changes=changes)
            await self._store.async_save(self.data)
            return await self.async_snapshot()

    async def async_sync_unifi(self, matches: dict[str, dict[str, Any]]) -> bool:
        """Persist network topology returned by UniFi for matching devices."""
        async with self._lock:
            changed = False
            fields = ("network", "vlan", "ssid", "connected_device", "switch_port")
            for device in self.data["devices"]:
                item = matches.get(str(device["id"]))
                if not item:
                    continue
                previous = deepcopy(device)
                for field in fields:
                    value = str(item.get(field, "") or "").strip()[:1000]
                    if value:
                        device[field] = value
                changes = self._device_changes(previous, device)
                if changes:
                    device["updated_at"] = _now()
                    self._record_log("update", device=device, changes=changes, source="unifi")
                    changed = True
            if changed:
                await self._store.async_save(self.data)
            return changed

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

    def _remember_tags(self, tags: list[str]) -> None:
        current = {item.casefold() for item in self.data["tags"]}
        for tag in tags:
            if tag.casefold() not in current:
                self.data["tags"].append(tag)
                current.add(tag.casefold())
        self.data["tags"].sort(key=str.casefold)

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
            "ha_device_kind",
            "parent_ha_device_id",
            "parent_device_name",
            "ha_config_entry_id",
            "ha_config_subentry_id",
            "battery_entity_id",
            "battery_last_replaced_at",
            "primary_entity_id",
            "integration",
            "unifi_id",
            "unifi_kind",
            "unifi_site_id",
            "network",
            "vlan",
            "ssid",
            "connected_device",
            "switch_port",
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
        }
        if cleaned["ha_device_kind"] != "child":
            required["mac"] = "MAC / IEEE"
        missing = [label for key, label in required.items() if not cleaned[key]]
        if (
            cleaned["ha_device_kind"] != "child"
            and cleaned["protocol"] in IP_PROTOCOLS
            and not cleaned["ip_address"]
        ):
            missing.append("IP address")
        if missing:
            raise InventoryError("Required fields: " + ", ".join(missing))
        cleaned["status"] = cleaned["status"] or "unknown"
        raw_tags = payload.get("tags", [])
        if isinstance(raw_tags, str):
            raw_tags = [item.strip() for item in raw_tags.split(",")]
        if not isinstance(raw_tags, list):
            raise InventoryError("Tags must be a list")
        canonical = {tag.casefold(): tag for tag in self.data["tags"]}
        cleaned["tags"] = sorted(
            {
                canonical.get(str(tag).strip().casefold(), str(tag).strip()[:60])
                for tag in raw_tags
                if str(tag).strip()
            },
            key=str.casefold,
        )
        cleaned["battery_history"] = self._clean_battery_history(
            payload.get("battery_history", [])
        )
        if cleaned["battery_last_replaced_at"]:
            self._validate_battery_date(cleaned["battery_last_replaced_at"])
        if cleaned["primary_entity_id"]:
            domain, separator, object_id = cleaned["primary_entity_id"].partition(".")
            if not separator or not domain or not object_id:
                raise InventoryError("HA Primary entity must be a complete entity ID")
        return cleaned

    def _append_initial_battery_history(self, device: dict[str, Any]) -> None:
        replaced_at = device.get("battery_last_replaced_at", "")
        if replaced_at and not device.get("battery_history"):
            device["battery_history"] = [self._battery_history_entry(replaced_at)]

    def _battery_history_entry(self, replaced_at: str, note: str = "") -> dict[str, str]:
        self._validate_battery_date(replaced_at)
        return {
            "id": uuid4().hex,
            "replaced_at": replaced_at,
            "recorded_at": _now(),
            "note": str(note).strip()[:500],
        }

    def _clean_battery_history(self, history: Any) -> list[dict[str, str]]:
        if not isinstance(history, list):
            raise InventoryError("Battery history must be a list")
        cleaned: list[dict[str, str]] = []
        for item in history[-100:]:
            if not isinstance(item, dict):
                continue
            replaced_at = str(item.get("replaced_at", "")).strip()
            if not replaced_at:
                continue
            self._validate_battery_date(replaced_at)
            cleaned.append(
                {
                    "id": str(item.get("id") or uuid4().hex),
                    "replaced_at": replaced_at,
                    "recorded_at": str(item.get("recorded_at") or _now()),
                    "note": str(item.get("note", "")).strip()[:500],
                }
            )
        return cleaned

    @staticmethod
    def _validate_battery_date(value: str) -> None:
        try:
            datetime.strptime(value, "%Y-%m-%d")
        except ValueError as err:
            raise InventoryError("Battery replacement date must use YYYY-MM-DD") from err

    def _backup_data(self) -> dict[str, Any]:
        return deepcopy({key: value for key, value in self.data.items() if key != "backups"})

    def _create_backup(self, reason: str) -> dict[str, Any]:
        backup = {
            "id": uuid4().hex,
            "created_at": _now(),
            "reason": reason,
            "device_count": len(self.data["devices"]),
            "data": self._backup_data(),
        }
        self.data["backups"].insert(0, backup)
        del self.data["backups"][10:]
        return backup

    def _validate_restore(self, incoming: dict[str, Any]) -> dict[str, Any]:
        devices = incoming.get("devices")
        protocols = incoming.get("protocols")
        if not isinstance(devices, list) or not isinstance(protocols, dict) or not protocols:
            raise InventoryError("Backup must contain devices and protocols")
        candidate = deepcopy(incoming)
        candidate.setdefault("device_types", list(DEFAULT_DEVICE_TYPES))
        candidate.setdefault("brands", [])
        candidate.setdefault("tags", list(DEFAULT_TAGS))
        candidate.setdefault("logs", [])
        candidate.setdefault("counters", {})
        candidate.setdefault(
            "niimbot",
            {"device_id": "", "label_width_mm": 30, "label_height_mm": 15, "margin_mm": 1.5, "top_margin_mm": 2},
        )
        candidate["backups"] = []
        old_data = self.data
        self.data = candidate
        try:
            cleaned_devices: list[dict[str, Any]] = []
            codes: set[int] = set()
            for raw in devices:
                if not isinstance(raw, dict):
                    raise InventoryError("Invalid device in backup")
                cleaned = self._clean_device(raw)
                code = _to_int(raw.get("device_code"))
                if code is None or code in codes:
                    raise InventoryError("Backup contains an invalid or duplicate Device ID")
                config = protocols[cleaned["protocol"]]
                if not config["start"] <= code <= config["end"]:
                    raise InventoryError(f"Device code {code} is outside its protocol range")
                now = _now()
                cleaned.update(
                    {
                        "id": str(raw.get("id") or uuid4().hex),
                        "device_code": code,
                        "created_at": str(raw.get("created_at") or now),
                        "updated_at": str(raw.get("updated_at") or now),
                    }
                )
                cleaned_devices.append(cleaned)
                codes.add(code)
            candidate["devices"] = cleaned_devices
            candidate["logs"] = [item for item in candidate["logs"] if isinstance(item, dict)][-500:]
            candidate["tags"] = sorted({str(item).strip()[:60] for item in candidate["tags"] if str(item).strip()}, key=str.casefold)
            candidate["brands"] = sorted({str(item).strip()[:100] for item in candidate["brands"] if str(item).strip()}, key=str.casefold)
            for key, config in protocols.items():
                used = [device["device_code"] for device in cleaned_devices if device["protocol"] == key]
                candidate["counters"][key] = max(candidate["counters"].get(key, config["start"] - 1), max(used, default=config["start"] - 1))
            return candidate
        finally:
            self.data = old_data

    def _record_log(
        self,
        action: str,
        *,
        device: dict[str, Any] | None = None,
        changes: list[dict[str, Any]] | None = None,
        source: str = "manual",
        details: str = "",
    ) -> None:
        self.data["logs"].append(
            {
                "id": uuid4().hex,
                "timestamp": _now(),
                "action": action,
                "source": source,
                "device_id": str(device.get("id", "")) if device else "",
                "device_code": device.get("device_code", "") if device else "",
                "device_name": str(device.get("name", "")) if device else "",
                "changes": changes or [],
                "details": details,
            }
        )
        self.data["logs"] = self.data["logs"][-500:]

    @staticmethod
    def _device_changes(before: dict[str, Any], after: dict[str, Any]) -> list[dict[str, Any]]:
        ignored = {"id", "created_at", "updated_at"}
        return [
            {"field": key, "old": deepcopy(before.get(key, "")), "new": deepcopy(after.get(key, ""))}
            for key in sorted((set(before) | set(after)) - ignored)
            if before.get(key, "") != after.get(key, "")
        ]


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
