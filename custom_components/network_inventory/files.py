"""Attachment and full-backup file helpers."""

from __future__ import annotations

from datetime import UTC, datetime
from io import BytesIO
import json
import os
from pathlib import Path
import shutil
from typing import Any
from uuid import uuid4
from zipfile import ZIP_DEFLATED, BadZipFile, ZipFile

from .const import MAX_BACKUP_SIZE
from .storage import InventoryError


def stored_attachment_name(attachment_id: str, original_name: str) -> str:
    """Return a filesystem-safe private attachment filename."""
    suffix = Path(original_name).suffix.lower()
    if len(suffix) > 12 or any(not (char.isalnum() or char == ".") for char in suffix):
        suffix = ""
    return f"{attachment_id}{suffix}"


def build_full_backup(payload: dict[str, Any], attachments_dir: Path) -> bytes:
    """Build a ZIP containing the JSON export and every declared attachment."""
    output = BytesIO()
    total_size = 0
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        archive.writestr(
            "inventory.json",
            json.dumps(payload, ensure_ascii=False, indent=2),
        )
        for device in payload.get("data", {}).get("devices", []):
            device_id = _safe_component(device.get("id", ""))
            for attachment in device.get("attachments", []):
                stored_name = _safe_component(attachment.get("stored_name", ""))
                if not device_id or not stored_name:
                    continue
                source = attachments_dir / device_id / stored_name
                if not source.is_file():
                    raise InventoryError(f"Attachment file is missing: {attachment['name']}")
                total_size += source.stat().st_size
                if total_size > MAX_BACKUP_SIZE:
                    raise InventoryError("The full backup exceeds 100 MB")
                archive.write(source, f"attachments/{device_id}/{stored_name}")
    return output.getvalue()


def parse_full_backup(data: bytes) -> tuple[dict[str, Any], dict[str, bytes]]:
    """Validate and read a Network Inventory full ZIP backup."""
    try:
        with ZipFile(BytesIO(data), "r") as archive:
            infos = archive.infolist()
            if sum(info.file_size for info in infos) > MAX_BACKUP_SIZE:
                raise InventoryError("The uncompressed backup is too large")
            names = {info.filename for info in infos if not info.is_dir()}
            if "inventory.json" not in names:
                raise InventoryError("The ZIP backup does not contain inventory.json")
            payload = json.loads(archive.read("inventory.json").decode("utf-8"))
            if (
                not isinstance(payload, dict)
                or not isinstance(payload.get("data"), dict)
                or not isinstance(payload["data"].get("devices"), list)
            ):
                raise InventoryError("The ZIP backup contains invalid inventory data")
            files: dict[str, bytes] = {}
            for info in infos:
                if info.is_dir() or info.filename == "inventory.json":
                    continue
                parts = Path(info.filename).parts
                if len(parts) != 3 or parts[0] != "attachments":
                    raise InventoryError("The ZIP backup contains an invalid path")
                device_id = _safe_component(parts[1])
                stored_name = _safe_component(parts[2])
                if not device_id or not stored_name:
                    raise InventoryError("The ZIP backup contains an invalid attachment path")
                relative = f"{device_id}/{stored_name}"
                if relative in files:
                    raise InventoryError("The ZIP backup contains duplicate attachments")
                files[relative] = archive.read(info)
    except (BadZipFile, UnicodeDecodeError, json.JSONDecodeError) as err:
        raise InventoryError("Invalid Network Inventory ZIP backup") from err

    declared: set[str] = set()
    for device in payload.get("data", {}).get("devices", []):
        if not isinstance(device, dict):
            raise InventoryError("The ZIP backup contains invalid device data")
        device_id = _safe_component(device.get("id", ""))
        attachments = device.get("attachments", [])
        if not isinstance(attachments, list):
            raise InventoryError("The ZIP backup contains invalid attachment data")
        for attachment in attachments:
            if not isinstance(attachment, dict):
                raise InventoryError("The ZIP backup contains invalid attachment data")
            stored_name = _safe_component(attachment.get("stored_name", ""))
            relative = f"{device_id}/{stored_name}"
            if relative in declared:
                raise InventoryError("The ZIP backup contains duplicate attachments")
            try:
                expected_size = max(0, int(attachment.get("size", 0)))
            except (TypeError, ValueError) as err:
                raise InventoryError("The ZIP backup contains invalid attachment data") from err
            if relative in files and len(files[relative]) != expected_size:
                raise InventoryError("The ZIP backup contains an attachment size mismatch")
            declared.add(relative)
    missing = declared - files.keys()
    if missing:
        raise InventoryError("The ZIP backup is missing one or more attachments")
    if files.keys() - declared:
        raise InventoryError("The ZIP backup contains undeclared attachments")
    return payload, files


def stage_attachment_restore(
    attachments_dir: Path, files: dict[str, bytes]
) -> tuple[Path, Path | None]:
    """Atomically install a restored attachment tree and retain the old tree."""
    parent = attachments_dir.parent
    parent.mkdir(parents=True, exist_ok=True)
    staging = parent / f"attachments-restore-{uuid4().hex}"
    previous = parent / f"attachments-previous-{uuid4().hex}"
    staging.mkdir()
    try:
        for relative, content in files.items():
            device_id, stored_name = relative.split("/", 1)
            target_dir = staging / _safe_component(device_id)
            target_dir.mkdir(exist_ok=True)
            (target_dir / _safe_component(stored_name)).write_bytes(content)
        old_path: Path | None = None
        if attachments_dir.exists():
            os.replace(attachments_dir, previous)
            old_path = previous
        os.replace(staging, attachments_dir)
        return attachments_dir, old_path
    except Exception:
        shutil.rmtree(staging, ignore_errors=True)
        if previous.exists() and not attachments_dir.exists():
            os.replace(previous, attachments_dir)
        raise


def rollback_attachment_restore(attachments_dir: Path, previous: Path | None) -> None:
    """Roll back a staged attachment replacement."""
    shutil.rmtree(attachments_dir, ignore_errors=True)
    if previous is not None and previous.exists():
        os.replace(previous, attachments_dir)


def finish_attachment_restore(previous: Path | None) -> None:
    """Remove the previous tree after a successful restore."""
    if previous is not None:
        shutil.rmtree(previous, ignore_errors=True)


def _safe_component(value: Any) -> str:
    text = str(value or "")
    if not text or text in {".", ".."} or Path(text).name != text:
        raise InventoryError("Invalid attachment path")
    return text


def backup_filename() -> str:
    """Return a dated full-backup filename."""
    return f"network-inventory-full-{datetime.now(UTC).date().isoformat()}.zip"
