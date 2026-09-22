"""Native Home Assistant firmware update helpers."""

from __future__ import annotations

from typing import Any, Iterable


def select_firmware_entries(
    entries: Iterable[Any], platform: str, excluded_translation_keys: set[str] | None = None
) -> dict[str, Any]:
    """Select one firmware update entity per HA device for an integration."""
    excluded = excluded_translation_keys or set()
    candidates = sorted(
        (
            entry
            for entry in entries
            if entry.device_id
            and entry.entity_id.startswith("update.")
            and entry.platform == platform
            and getattr(entry, "translation_key", None) not in excluded
        ),
        key=lambda entry: (entry.disabled_by is not None, entry.entity_id),
    )
    selected: dict[str, Any] = {}
    for entry in candidates:
        selected.setdefault(entry.device_id, entry)
    return selected


def select_shelly_firmware_entries(entries: Iterable[Any]) -> dict[str, Any]:
    """Select one stable Shelly firmware update entity per HA device."""
    return select_firmware_entries(
        entries, "shelly", {"beta_firmware", "lora_firmware"}
    )


def select_reolink_firmware_entries(entries: Iterable[Any]) -> dict[str, Any]:
    """Select the Reolink firmware update entity for each HA device."""
    return select_firmware_entries(entries, "reolink")


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
        "firmware_integration": entry.platform,
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


def native_integration_status(
    config_entries: Iterable[Any],
    updates: dict[str, dict[str, Any]],
    device_count: int | None = None,
) -> dict[str, Any]:
    """Summarize a native Home Assistant integration with firmware entities."""
    entries = list(config_entries)
    firmware_entities = list(updates.values())
    return {
        "native": True,
        "configured": bool(entries),
        "device_count": len(entries) if device_count is None else device_count,
        "firmware_entity_count": len(firmware_entities),
        "active_firmware_entity_count": sum(
            not item["firmware_update_disabled"] for item in firmware_entities
        ),
        "updates_available": sum(
            item["firmware_update_available"] for item in firmware_entities
        ),
    }


def shelly_integration_status(
    config_entries: Iterable[Any],
    updates: dict[str, dict[str, Any]],
    device_count: int | None = None,
) -> dict[str, Any]:
    """Summarize the native Home Assistant Shelly integration."""
    return native_integration_status(config_entries, updates, device_count)


def reolink_integration_status(
    config_entries: Iterable[Any],
    updates: dict[str, dict[str, Any]],
    device_count: int | None = None,
) -> dict[str, Any]:
    """Summarize the native Home Assistant Reolink integration."""
    return native_integration_status(config_entries, updates, device_count)
