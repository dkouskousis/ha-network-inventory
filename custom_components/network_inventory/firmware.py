"""Shelly firmware update helpers."""

from __future__ import annotations

from typing import Any, Iterable


def select_shelly_firmware_entries(entries: Iterable[Any]) -> dict[str, Any]:
    """Select one stable Shelly firmware update entity per HA device."""
    candidates = sorted(
        (
            entry
            for entry in entries
            if entry.device_id
            and entry.entity_id.startswith("update.")
            and entry.platform == "shelly"
            and getattr(entry, "translation_key", None)
            not in {"beta_firmware", "lora_firmware"}
        ),
        key=lambda entry: (entry.disabled_by is not None, entry.entity_id),
    )
    selected: dict[str, Any] = {}
    for entry in candidates:
        selected.setdefault(entry.device_id, entry)
    return selected


def firmware_update_details(entry: Any, state: Any) -> dict[str, Any]:
    """Build the frontend firmware status for one update registry entry."""
    attributes = state.attributes if state else {}
    in_progress = attributes.get("in_progress", False)
    percentage = attributes.get("update_percentage")
    if percentage is None and isinstance(in_progress, (int, float)) and not isinstance(
        in_progress, bool
    ):
        percentage = in_progress
    return {
        "firmware_update_entity_id": entry.entity_id,
        "firmware_update_disabled": entry.disabled_by is not None,
        "firmware_update_available": bool(state and state.state == "on"),
        "firmware_update_in_progress": bool(in_progress),
        "firmware_update_percentage": percentage,
        "firmware_installed_version": str(attributes.get("installed_version") or ""),
        "firmware_latest_version": str(attributes.get("latest_version") or ""),
        "firmware_release_url": str(attributes.get("release_url") or ""),
        "firmware_available": bool(
            state and state.state not in {"unknown", "unavailable"}
        ),
    }


def shelly_integration_status(
    config_entries: Iterable[Any], updates: dict[str, dict[str, Any]]
) -> dict[str, Any]:
    """Summarize the native Home Assistant Shelly integration."""
    entries = list(config_entries)
    firmware_entities = list(updates.values())
    return {
        "native": True,
        "configured": bool(entries),
        "device_count": len(entries),
        "firmware_entity_count": len(firmware_entities),
        "active_firmware_entity_count": sum(
            not item["firmware_update_disabled"] for item in firmware_entities
        ),
        "updates_available": sum(
            item["firmware_update_available"] for item in firmware_entities
        ),
    }
