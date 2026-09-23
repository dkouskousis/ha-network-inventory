"""Persistent inventory storage."""

from __future__ import annotations

import asyncio
from copy import deepcopy
from datetime import UTC, datetime
from pathlib import Path
import shutil
from typing import Any
from uuid import uuid4

from homeassistant.core import HomeAssistant
from homeassistant.helpers.storage import Store

from .const import (
    CUSTOM_FIELD_TYPES,
    ATTACHMENTS_DIR,
    DEFAULT_DEVICE_TYPES,
    DEFAULT_GENERAL_SETTINGS,
    DEFAULT_PROTOCOLS,
    DEFAULT_LABELS,
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


def _clean_general_settings(value: Any) -> dict[str, str]:
    """Validate regional display preferences."""
    if not isinstance(value, dict):
        raise InventoryError("General settings must be an object")
    time_format = str(value.get("time_format", ""))
    date_format = str(value.get("date_format", ""))
    if time_format not in {"24h", "12h"}:
        raise InventoryError("Time format must be 24h or 12h")
    if date_format not in {"day_first", "month_first"}:
        raise InventoryError("Date format must be day first or month first")
    return {"time_format": time_format, "date_format": date_format}


class InventoryStore:
    """Manage the inventory and its monotonically increasing IDs."""

    def __init__(self, hass: HomeAssistant) -> None:
        self._store: Store[dict[str, Any]] = Store(
            hass, STORAGE_VERSION, STORAGE_KEY, private=True, atomic_writes=True
        )
        self._lock = asyncio.Lock()
        self.data: dict[str, Any] = {}
        self.attachments_dir = (
            Path(hass.config.path(ATTACHMENTS_DIR)) if hass is not None else None
        )

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
            "labels": list(DEFAULT_LABELS),
            "logs": [],
            "notes": [],
            "backups": [],
            "counters": {
                key: value["start"] - 1 for key, value in DEFAULT_PROTOCOLS.items()
            },
        }
        self.data.setdefault("devices", [])
        self.data.setdefault("protocols", deepcopy(DEFAULT_PROTOCOLS))
        self.data.setdefault("device_types", list(DEFAULT_DEVICE_TYPES))
        if "labels" not in self.data:
            self.data["labels"] = self.data.pop("tags", list(DEFAULT_LABELS))
            migrated = True
        else:
            self.data.pop("tags", None)
        self.data.setdefault("logs", [])
        if "notes" not in self.data:
            self.data["notes"] = []
            migrated = True
        self.data.setdefault("backups", [])
        if "custom_fields" not in self.data:
            self.data["custom_fields"] = []
            migrated = True
        self.data["custom_fields"] = self._clean_custom_fields(
            self.data["custom_fields"]
        )
        self.data.setdefault("ha_labels_migrated", False)
        previous_general = deepcopy(self.data.get("general"))
        self.data.setdefault("general", deepcopy(DEFAULT_GENERAL_SETTINGS))
        for key, value in DEFAULT_GENERAL_SETTINGS.items():
            self.data["general"].setdefault(key, value)
        self.data["general"] = _clean_general_settings(self.data["general"])
        if previous_general != self.data["general"]:
            migrated = True
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
            if "labels" not in device:
                device["labels"] = device.pop("tags", [])
                migrated = True
            else:
                device.pop("tags", None)
            device.setdefault("battery_entity_id", "")
            device.setdefault("battery_last_replaced_at", "")
            device.setdefault("battery_history", [])
            device.setdefault("primary_entity_id", "")
            for key in ("purchase_date", "purchase_store", "serial_number", "warranty_end_date", "receipt_attachment_id"):
                if key not in device:
                    device[key] = ""
                    migrated = True
            for key, default in (
                ("admin_url", ""),
                ("links", []),
                ("custom_values", {}),
                ("attachments", []),
            ):
                if key not in device:
                    device[key] = deepcopy(default)
                    migrated = True
            cleaned_admin_url = str(device.get("admin_url", "")).strip()[:1000]
            if cleaned_admin_url:
                self._validate_http_url(cleaned_admin_url, "Admin URL")
            cleaned_links = self._clean_links(device.get("links", []))
            cleaned_values = self._clean_custom_values(
                device.get("custom_values", {})
            )
            cleaned_attachments = self._clean_attachments(
                device.get("attachments", [])
            )
            if (
                device["admin_url"] != cleaned_admin_url
                or device["links"] != cleaned_links
                or device["custom_values"] != cleaned_values
                or device["attachments"] != cleaned_attachments
            ):
                migrated = True
            device["admin_url"] = cleaned_admin_url
            device["links"] = cleaned_links
            device["custom_values"] = cleaned_values
            device["attachments"] = cleaned_attachments
        self.data["notes"] = [self._clean_note(note) for note in self.data["notes"]]
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

    async def async_sync_ha_labels(
        self,
        labels: list[str],
        device_labels: dict[str, list[str]],
        *,
        migrated: bool = True,
    ) -> bool:
        """Store labels and assignments read from Home Assistant."""
        async with self._lock:
            changed = False
            cleaned_labels = sorted(
                {str(label).strip()[:60] for label in labels if str(label).strip()},
                key=str.casefold,
            )
            if self.data["labels"] != cleaned_labels:
                self.data["labels"] = cleaned_labels
                changed = True
            available_labels = {label.casefold() for label in cleaned_labels}
            for note in self.data["notes"]:
                retained = [label for label in note["labels"] if label.casefold() in available_labels]
                if retained != note["labels"]:
                    note["labels"] = retained
                    note["updated_at"] = _now()
                    changed = True
            for device in self.data["devices"]:
                if device["id"] not in device_labels:
                    continue
                synced_labels = sorted(
                    {
                        str(label).strip()[:60]
                        for label in device_labels[device["id"]]
                        if str(label).strip()
                    },
                    key=str.casefold,
                )
                if device.get("labels", []) == synced_labels:
                    continue
                previous = list(device.get("labels", []))
                device["labels"] = synced_labels
                device["updated_at"] = _now()
                self._record_log(
                    "update",
                    device=device,
                    changes=[{"field": "labels", "old": previous, "new": synced_labels}],
                    source="home_assistant",
                )
                changed = True
            if migrated and not self.data.get("ha_labels_migrated"):
                self.data["ha_labels_migrated"] = True
                changed = True
            if changed:
                await self._store.async_save(self.data)
            return changed

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
            # Attachment metadata is managed only after the file is safely stored.
            device["attachments"] = []
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
            self._remember_labels(device["labels"])
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
            updated = self._clean_device(
                {**device, **payload, "attachments": device.get("attachments", [])}
            )
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
            self._remember_labels(device["labels"])
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
            previous = deepcopy(device)
            replacement = self._battery_history_entry(replaced_at, note)
            device.setdefault("battery_history", []).append(replacement)
            device["battery_last_replaced_at"] = replacement["replaced_at"]
            device["updated_at"] = _now()
            self._record_log(
                "battery_replaced",
                device=device,
                changes=self._device_changes(previous, device),
                details=f"Battery replaced on {replacement['replaced_at']}",
                source="battery",
            )
            await self._store.async_save(self.data)
            return deepcopy(device)

    async def async_undo_log(self, log_id: str) -> dict[str, Any]:
        """Safely revert a device change recorded in the audit log."""
        async with self._lock:
            log = next(
                (item for item in self.data["logs"] if item.get("id") == log_id),
                None,
            )
            if log is None:
                raise InventoryError("Log entry not found")
            if log.get("action") not in {"update", "bulk_update", "battery_replaced"}:
                raise InventoryError("This log entry cannot be undone")
            if log.get("undone_by"):
                raise InventoryError("This change has already been undone")
            changes = log.get("changes")
            if not isinstance(changes, list) or not changes:
                raise InventoryError("This log entry has no reversible changes")

            device = self._find(str(log.get("device_id") or ""))
            for change in changes:
                field = str(change.get("field") or "")
                if not field or device.get(field, "") != change.get("new", ""):
                    raise InventoryError(
                        "The device changed after this log entry and cannot be safely undone"
                    )

            previous = deepcopy(device)
            payload = deepcopy(device)
            for change in changes:
                payload[str(change["field"])] = deepcopy(change.get("old", ""))
            reverted = self._clean_device(payload)
            protected = {
                "id": device["id"],
                "device_code": device["device_code"],
                "created_at": device["created_at"],
            }
            reverted.update(protected)
            reverted["protocol"] = self._normalise_protocol(reverted.get("protocol"))
            reverted["updated_at"] = _now()
            actual_changes = self._device_changes(previous, reverted)
            if not actual_changes:
                raise InventoryError("This log entry has no reversible changes")
            device.clear()
            device.update(reverted)
            self._remember_brand(device["brand"])
            self._remember_labels(device["labels"])
            undo_log = self._record_log(
                "undo",
                device=device,
                changes=actual_changes,
                source="logs",
                details=f"Reverted log {log_id}",
                reverts_log_id=log_id,
            )
            log["undone_by"] = undo_log["id"]
            await self._store.async_save(self.data)
            return deepcopy(device)

    async def async_bulk_update(
        self,
        device_ids: list[str],
        fields: dict[str, Any],
        label_mode: str = "",
        labels: list[str] | None = None,
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
        if label_mode not in {"", "add", "remove", "replace"}:
            raise InventoryError("Invalid bulk label operation")
        if not fields and not label_mode:
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
                requested_labels = {
                    str(label).strip()[:60] for label in (labels or []) if str(label).strip()
                }
                for device in devices:
                    payload = {**device, **fields}
                    current_labels = set(device.get("labels", []))
                    if label_mode == "add":
                        payload["labels"] = sorted(current_labels | requested_labels, key=str.casefold)
                    elif label_mode == "remove":
                        remove = {label.casefold() for label in requested_labels}
                        payload["labels"] = [
                            label for label in current_labels if label.casefold() not in remove
                        ]
                    elif label_mode == "replace":
                        payload["labels"] = sorted(requested_labels, key=str.casefold)

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
                    self._remember_labels(device["labels"])
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
            for note in self.data["notes"]:
                if note["device_id"] == internal_id:
                    note["device_id"] = ""
                    note["updated_at"] = _now()
            self._record_log("delete", device=device, changes=self._device_changes(device, {}))
            self.data["devices"].remove(device)
            await self._store.async_save(self.data)
        if self.attachments_dir is not None:
            target = self.attachments_dir / internal_id
            await asyncio.to_thread(shutil.rmtree, target, True)

    async def async_get_device(self, internal_id: str) -> dict[str, Any]:
        """Return one stored device."""
        async with self._lock:
            return deepcopy(self._find(internal_id))

    def _find_note(self, note_id: str) -> dict[str, Any]:
        for note in self.data["notes"]:
            if note["id"] == note_id:
                return note
        raise InventoryError("Note not found")

    def _clean_note(self, note: dict[str, Any]) -> dict[str, Any]:
        if not isinstance(note, dict):
            raise InventoryError("Invalid note")
        body = str(note.get("body", "")).strip()
        if not body or len(body) > 20000:
            raise InventoryError("Note text is required (up to 20000 characters)")
        device_id = str(note.get("device_id", "")).strip()
        if device_id and not any(device["id"] == device_id for device in self.data["devices"]):
            raise InventoryError("Device not found")
        labels = note.get("labels", [])
        if not isinstance(labels, list):
            raise InventoryError("Labels must be a list")
        available = {label.casefold(): label for label in self.data["labels"]}
        if any(str(label).casefold() not in available for label in labels):
            raise InventoryError("Choose existing labels")
        note_id = str(note.get("id", "")).strip()
        if note_id and (len(note_id) > 64 or not all(char.isalnum() or char in "-_" for char in note_id)):
            raise InventoryError("Invalid note ID")
        return {
            "id": note_id or uuid4().hex,
            "title": str(note.get("title", "")).strip()[:200],
            "body": body,
            "device_id": device_id,
            "labels": sorted({available[str(label).casefold()] for label in labels}, key=str.casefold),
            "attachments": self._clean_attachments(note.get("attachments", [])),
            "created_at": str(note.get("created_at") or _now()),
            "updated_at": str(note.get("updated_at") or _now()),
        }

    async def async_save_note(self, payload: dict[str, Any], note_id: str = "") -> dict[str, Any]:
        async with self._lock:
            previous = self._find_note(note_id) if note_id else None
            candidate = {**previous, **payload} if previous else {**payload, "id": "", "created_at": "", "updated_at": ""}
            cleaned = self._clean_note(candidate)
            if previous:
                cleaned["id"] = previous["id"]
                cleaned["created_at"] = previous["created_at"]
                cleaned["attachments"] = previous["attachments"]
                cleaned["updated_at"] = _now()
                previous.update(cleaned)
            else:
                cleaned["attachments"] = []
                self.data["notes"].append(cleaned)
            await self._store.async_save(self.data)
            return deepcopy(cleaned)

    async def async_delete_note(self, note_id: str) -> None:
        async with self._lock:
            note = self._find_note(note_id)
            self.data["notes"].remove(note)
            await self._store.async_save(self.data)
        if self.attachments_dir is not None:
            await asyncio.to_thread(shutil.rmtree, self.attachments_dir / f"note-{note_id}", True)

    async def async_get_note(self, note_id: str) -> dict[str, Any]:
        async with self._lock:
            return deepcopy(self._find_note(note_id))

    async def async_add_note_attachment(self, note_id: str, attachment: dict[str, Any]) -> dict[str, Any]:
        async with self._lock:
            note = self._find_note(note_id)
            if len(note["attachments"]) >= 100:
                raise InventoryError("A note can have up to 100 attachments")
            cleaned = self._clean_attachments([attachment])[0]
            note["attachments"].append(cleaned)
            note["updated_at"] = _now()
            await self._store.async_save(self.data)
            return deepcopy(cleaned)

    async def async_remove_note_attachment(self, note_id: str, attachment_id: str) -> dict[str, Any]:
        async with self._lock:
            note = self._find_note(note_id)
            attachment = next((item for item in note["attachments"] if item["id"] == attachment_id), None)
            if attachment is None:
                raise InventoryError("Attachment not found")
            note["attachments"].remove(attachment)
            note["updated_at"] = _now()
            await self._store.async_save(self.data)
            return deepcopy(attachment)

    async def async_add_attachment(
        self, internal_id: str, attachment: dict[str, Any]
    ) -> dict[str, Any]:
        """Add attachment metadata after its file has been stored."""
        async with self._lock:
            device = self._find(internal_id)
            cleaned = self._clean_attachments([attachment])
            if not cleaned:
                raise InventoryError("Invalid attachment")
            device.setdefault("attachments", []).append(cleaned[0])
            device["updated_at"] = _now()
            self._record_log(
                "attachment_add",
                device=device,
                details=f"Attachment added: {cleaned[0]['name']}",
                source="attachment",
            )
            await self._store.async_save(self.data)
            return deepcopy(cleaned[0])

    async def async_remove_attachment(
        self, internal_id: str, attachment_id: str
    ) -> dict[str, Any]:
        """Remove attachment metadata and return the removed item."""
        async with self._lock:
            device = self._find(internal_id)
            attachment = next(
                (
                    item
                    for item in device.get("attachments", [])
                    if item.get("id") == attachment_id
                ),
                None,
            )
            if attachment is None:
                raise InventoryError("Attachment not found")
            device["attachments"].remove(attachment)
            if device.get("receipt_attachment_id") == attachment_id:
                device["receipt_attachment_id"] = ""
            device["updated_at"] = _now()
            self._record_log(
                "attachment_delete",
                device=device,
                details=f"Attachment removed: {attachment['name']}",
                source="attachment",
            )
            await self._store.async_save(self.data)
            return deepcopy(attachment)

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
                device["attachments"] = []
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
                self._remember_labels(device["labels"])
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
        """Save general preferences, protocol ranges, and field options."""
        async with self._lock:
            previous = {
                "general": deepcopy(self.data["general"]),
                "protocols": deepcopy(self.data["protocols"]),
                "device_types": deepcopy(self.data["device_types"]),
                "brands": deepcopy(self.data["brands"]),
                "labels": deepcopy(self.data["labels"]),
                "custom_fields": deepcopy(self.data["custom_fields"]),
            }
            general = _clean_general_settings(
                payload.get("general", self.data["general"])
            )
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

            labels = {
                str(item).strip()[:60]
                for item in payload.get("labels", self.data["labels"])
                if str(item).strip()
            }
            labels.update(label for device in self.data["devices"] for label in device.get("labels", []))
            labels.update(label for note in self.data["notes"] for label in note.get("labels", []))

            custom_fields = self._clean_custom_fields(
                payload.get("custom_fields", self.data["custom_fields"])
            )
            custom_field_ids = {item["id"] for item in custom_fields}
            cleaned_custom_values = {
                device["id"]: self._clean_custom_values(
                    {
                        key: value
                        for key, value in device.get("custom_values", {}).items()
                        if key in custom_field_ids
                    },
                    custom_fields,
                )
                for device in self.data["devices"]
            }

            self.data["general"] = general
            self.data["protocols"] = cleaned
            self.data["device_types"] = device_types
            self.data["brands"] = sorted(brands, key=str.casefold)
            self.data["labels"] = sorted(labels, key=str.casefold)
            self.data["custom_fields"] = custom_fields
            for device in self.data["devices"]:
                device["custom_values"] = cleaned_custom_values[device["id"]]
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

    def _remember_labels(self, labels: list[str]) -> None:
        current = {item.casefold() for item in self.data["labels"]}
        for label in labels:
            if label.casefold() not in current:
                self.data["labels"].append(label)
                current.add(label.casefold())
        self.data["labels"].sort(key=str.casefold)

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
            "admin_url",
            "purchase_date",
            "purchase_store",
            "serial_number",
            "warranty_end_date",
            "receipt_attachment_id",
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
        raw_labels = payload.get("labels", [])
        if isinstance(raw_labels, str):
            raw_labels = [item.strip() for item in raw_labels.split(",")]
        if not isinstance(raw_labels, list):
            raise InventoryError("Labels must be a list")
        canonical = {label.casefold(): label for label in self.data["labels"]}
        cleaned["labels"] = sorted(
            {
                canonical.get(str(label).strip().casefold(), str(label).strip()[:60])
                for label in raw_labels
                if str(label).strip()
            },
            key=str.casefold,
        )
        cleaned["battery_history"] = self._clean_battery_history(
            payload.get("battery_history", [])
        )
        cleaned["links"] = self._clean_links(payload.get("links", []))
        cleaned["custom_values"] = self._clean_custom_values(
            payload.get("custom_values", {})
        )
        cleaned["attachments"] = self._clean_attachments(
            payload.get("attachments", [])
        )
        for key in ("purchase_date", "warranty_end_date"):
            if cleaned[key]:
                try:
                    datetime.strptime(cleaned[key], "%Y-%m-%d")
                except ValueError as err:
                    raise InventoryError(f"{key.replace('_', ' ').capitalize()} must use YYYY-MM-DD") from err
        if cleaned["receipt_attachment_id"] and not any(
            item["id"] == cleaned["receipt_attachment_id"] for item in cleaned["attachments"]
        ):
            raise InventoryError("Receipt must be one of this device's attachments")
        if cleaned["admin_url"]:
            self._validate_http_url(cleaned["admin_url"], "Admin URL")
        if cleaned["battery_last_replaced_at"]:
            self._validate_battery_date(cleaned["battery_last_replaced_at"])
        if cleaned["primary_entity_id"]:
            domain, separator, object_id = cleaned["primary_entity_id"].partition(".")
            if not separator or not domain or not object_id:
                raise InventoryError("HA Primary entity must be a complete entity ID")
        return cleaned

    def _clean_custom_fields(self, fields: Any) -> list[dict[str, str]]:
        if not isinstance(fields, list):
            raise InventoryError("Custom fields must be a list")
        cleaned: list[dict[str, str]] = []
        seen_ids: set[str] = set()
        seen_labels: set[str] = set()
        for item in fields[:50]:
            if not isinstance(item, dict):
                continue
            label = str(item.get("label", "")).strip()[:80]
            field_type = str(item.get("type", "text")).strip().lower()
            field_id = str(item.get("id") or uuid4().hex).strip()[:64]
            if not label:
                raise InventoryError("Every custom field needs a name")
            if field_type not in CUSTOM_FIELD_TYPES:
                raise InventoryError(f"Unsupported custom field type: {field_type}")
            if field_id in seen_ids or label.casefold() in seen_labels:
                raise InventoryError("Custom field names must be unique")
            seen_ids.add(field_id)
            seen_labels.add(label.casefold())
            cleaned.append({"id": field_id, "label": label, "type": field_type})
        return cleaned

    def _clean_custom_values(
        self,
        values: Any,
        definitions: list[dict[str, str]] | None = None,
    ) -> dict[str, Any]:
        if not isinstance(values, dict):
            raise InventoryError("Custom field values must be an object")
        fields = {
            item["id"]: item
            for item in (
                definitions
                if definitions is not None
                else self.data.get("custom_fields", [])
            )
        }
        cleaned: dict[str, Any] = {}
        for field_id, value in values.items():
            definition = fields.get(str(field_id))
            if definition is None:
                continue
            field_type = definition["type"]
            if field_type == "boolean":
                cleaned[field_id] = value is True or str(value).lower() in {"1", "true", "on", "yes"}
                continue
            text = str(value or "").strip()[:2000]
            if not text:
                continue
            if field_type == "number":
                try:
                    float(text)
                except ValueError as err:
                    raise InventoryError(f"{definition['label']} must be a number") from err
            elif field_type == "date":
                try:
                    datetime.strptime(text, "%Y-%m-%d")
                except ValueError as err:
                    raise InventoryError(f"{definition['label']} must use YYYY-MM-DD") from err
            elif field_type == "url":
                self._validate_http_url(text, definition["label"])
            cleaned[field_id] = text
        return cleaned

    def _clean_links(self, links: Any) -> list[dict[str, str]]:
        if not isinstance(links, list):
            raise InventoryError("Links must be a list")
        cleaned: list[dict[str, str]] = []
        for item in links[:25]:
            if not isinstance(item, dict):
                continue
            label = str(item.get("label", "")).strip()[:100]
            url = str(item.get("url", "")).strip()[:2000]
            if not label and not url:
                continue
            if not label or not url:
                raise InventoryError("Every link needs a name and URL")
            self._validate_http_url(url, label)
            cleaned.append({"id": str(item.get("id") or uuid4().hex), "label": label, "url": url})
        return cleaned

    @staticmethod
    def _clean_attachments(attachments: Any) -> list[dict[str, Any]]:
        if not isinstance(attachments, list):
            raise InventoryError("Attachments must be a list")
        if len(attachments) > 100:
            raise InventoryError("A device can have up to 100 attachments")
        cleaned: list[dict[str, Any]] = []
        seen_ids: set[str] = set()
        seen_names: set[str] = set()
        for item in attachments[:100]:
            if not isinstance(item, dict):
                continue
            attachment_id = str(item.get("id", "")).strip()
            name = str(item.get("name", "")).strip()[:255]
            stored_name = str(item.get("stored_name", "")).strip()[:100]
            if not attachment_id or not name or not stored_name:
                continue
            if stored_name in {".", ".."} or Path(stored_name).name != stored_name:
                raise InventoryError("Invalid attachment filename")
            if attachment_id in seen_ids or stored_name in seen_names:
                raise InventoryError("Duplicate attachment metadata")
            try:
                size = max(0, int(item.get("size", 0)))
            except (TypeError, ValueError) as err:
                raise InventoryError("Invalid attachment size") from err
            seen_ids.add(attachment_id)
            seen_names.add(stored_name)
            cleaned.append(
                {
                    "id": attachment_id,
                    "name": name,
                    "stored_name": stored_name,
                    "content_type": str(item.get("content_type", "application/octet-stream"))[:150],
                    "size": size,
                    "created_at": str(item.get("created_at") or _now()),
                }
            )
        return cleaned

    @staticmethod
    def _validate_http_url(value: str, label: str) -> None:
        from urllib.parse import urlparse

        parsed = urlparse(value)
        if parsed.scheme not in {"http", "https"} or not parsed.netloc:
            raise InventoryError(f"{label} must be a valid http or https URL")

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
        if "labels" not in candidate:
            candidate["labels"] = candidate.pop("tags", list(DEFAULT_LABELS))
        else:
            candidate.pop("tags", None)
        candidate.setdefault("logs", [])
        candidate.setdefault("notes", [])
        candidate.setdefault("custom_fields", [])
        candidate["custom_fields"] = self._clean_custom_fields(
            candidate["custom_fields"]
        )
        candidate.setdefault("counters", {})
        candidate.setdefault("ha_labels_migrated", False)
        candidate.setdefault("general", deepcopy(DEFAULT_GENERAL_SETTINGS))
        candidate["general"] = _clean_general_settings(candidate["general"])
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
                if "labels" not in raw and "tags" in raw:
                    raw = {**raw, "labels": raw["tags"]}
                cleaned = self._clean_device(raw)
                code = _to_int(raw.get("device_code"))
                if code is None or code in codes:
                    raise InventoryError("Backup contains an invalid or duplicate Device ID")
                config = protocols[cleaned["protocol"]]
                if not config["start"] <= code <= config["end"]:
                    raise InventoryError(f"Device code {code} is outside its protocol range")
                now = _now()
                internal_id = str(raw.get("id") or uuid4().hex)
                if (
                    not internal_id
                    or len(internal_id) > 64
                    or not all(char.isalnum() or char in {"-", "_"} for char in internal_id)
                ):
                    raise InventoryError("Backup contains an invalid internal device ID")
                cleaned.update(
                    {
                        "id": internal_id,
                        "device_code": code,
                        "created_at": str(raw.get("created_at") or now),
                        "updated_at": str(raw.get("updated_at") or now),
                    }
                )
                cleaned_devices.append(cleaned)
                codes.add(code)
            candidate["devices"] = cleaned_devices
            if not isinstance(candidate["notes"], list):
                raise InventoryError("Invalid notes in backup")
            if any(not isinstance(note, dict) or not note.get("id") for note in candidate["notes"]):
                raise InventoryError("Invalid note ID in backup")
            candidate["notes"] = [self._clean_note(note) for note in candidate["notes"]]
            if len({note["id"] for note in candidate["notes"]}) != len(candidate["notes"]):
                raise InventoryError("Duplicate note IDs in backup")
            candidate["logs"] = [item for item in candidate["logs"] if isinstance(item, dict)][-500:]
            candidate["labels"] = sorted({str(item).strip()[:60] for item in candidate["labels"] if str(item).strip()}, key=str.casefold)
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
        reverts_log_id: str = "",
    ) -> dict[str, Any]:
        log = {
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
        if reverts_log_id:
            log["reverts_log_id"] = reverts_log_id
        self.data["logs"].append(log)
        self.data["logs"] = self.data["logs"][-500:]
        return log

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
