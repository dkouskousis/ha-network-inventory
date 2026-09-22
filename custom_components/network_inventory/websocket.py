"""WebSocket API for Network Inventory."""

from __future__ import annotations

from ipaddress import ip_address
from typing import Any
from urllib.parse import urlparse

import voluptuous as vol

from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback
from homeassistant.exceptions import HomeAssistantError
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import label_registry as lr

from .const import DOMAIN, VERSION
from .firmware import firmware_update_details, select_shelly_firmware_entries
from .storage import InventoryError, InventoryStore, common_entity_name
from .unifi import UniFiCloudManager, UniFiError, match_unifi_items


def async_register_commands(hass: HomeAssistant) -> None:
    """Register the frontend API."""
    websocket_api.async_register_command(hass, websocket_list)
    websocket_api.async_register_command(hass, websocket_add)
    websocket_api.async_register_command(hass, websocket_update)
    websocket_api.async_register_command(hass, websocket_battery_replaced)
    websocket_api.async_register_command(hass, websocket_bulk_update)
    websocket_api.async_register_command(hass, websocket_delete)
    websocket_api.async_register_command(hass, websocket_import)
    websocket_api.async_register_command(hass, websocket_export)
    websocket_api.async_register_command(hass, websocket_restore)
    websocket_api.async_register_command(hass, websocket_restore_backup)
    websocket_api.async_register_command(hass, websocket_settings)
    websocket_api.async_register_command(hass, websocket_unifi_connect)
    websocket_api.async_register_command(hass, websocket_unifi_disconnect)
    websocket_api.async_register_command(hass, websocket_unifi_refresh)
    websocket_api.async_register_command(hass, websocket_niimbot_configure)
    websocket_api.async_register_command(hass, websocket_niimbot_print)


def _manager(hass: HomeAssistant) -> InventoryStore:
    return hass.data[DOMAIN]["manager"]


def _unifi(hass: HomeAssistant) -> UniFiCloudManager:
    return hass.data[DOMAIN]["unifi"]


@callback
def _niimbot_printers(hass: HomeAssistant) -> list[dict[str, str]]:
    """Return NIIMBOT devices already configured in Home Assistant."""
    registry = dr.async_get(hass)
    entry_ids = {entry.entry_id for entry in hass.config_entries.async_entries("niimbot")}
    printers = [
        {
            "device_id": device.id,
            "name": device.name_by_user or device.name or device.model or "NIIMBOT",
            "model": device.model or "",
        }
        for device in registry.devices
        if device.config_entry_id in entry_ids
    ]
    return sorted(printers, key=lambda item: item["name"].casefold())


@callback
def _niimbot_status(
    hass: HomeAssistant, settings: dict[str, Any]
) -> dict[str, Any]:
    """Return NIIMBOT availability and the selected printer."""
    printers = _niimbot_printers(hass)
    selected = str(settings.get("device_id") or "")
    return {
        "installed": bool(hass.config_entries.async_entries("niimbot")),
        "printers": printers,
        "device_id": selected,
        "label_width_mm": settings.get("label_width_mm", 30),
        "label_height_mm": settings.get("label_height_mm", 15),
        "margin_mm": settings.get("margin_mm", 1.5),
        "top_margin_mm": settings.get("top_margin_mm", 2),
        "connected": bool(selected and any(item["device_id"] == selected for item in printers)),
    }


@websocket_api.websocket_command({"type": f"{DOMAIN}/list"})
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_list(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Return inventory data and importable HA devices."""
    await async_sync_labels_from_home_assistant(hass)
    data = await _manager(hass).async_snapshot()
    await _unifi(hass).async_ensure_loaded()
    unifi_matches, unifi_items = match_unifi_items(data["devices"], _unifi(hass).items)
    if await _manager(hass).async_sync_unifi(unifi_matches):
        data = await _manager(hass).async_snapshot()
        unifi_matches, unifi_items = match_unifi_items(data["devices"], _unifi(hass).items)
    data["integrations"] = {
        "unifi": _unifi(hass).status(),
        "niimbot": _niimbot_status(hass, data.get("niimbot", {})),
    }
    data["unifi_items"] = unifi_items
    data["unifi_matches"] = unifi_matches
    data["ha_devices"] = _home_assistant_devices(hass, data["devices"])
    data["ha_entities"] = _home_assistant_entities(hass)
    data["battery_entities"] = _battery_entities(hass)
    firmware_updates = _shelly_firmware_updates(hass)
    battery_by_device: dict[str, list[str]] = {}
    for item in data["battery_entities"]:
        if item["device_id"]:
            battery_by_device.setdefault(item["device_id"], []).append(
                item["entity_id"]
            )
    for device in data["ha_devices"]:
        candidates = battery_by_device.get(device["ha_device_id"], [])
        device["battery_entity_id"] = candidates[0] if len(candidates) == 1 else ""
    entity_device_ids = {
        item["entity_id"]: item["device_id"] for item in data["ha_entities"]
    }
    entity_registry = er.async_get(hass)
    for device in data["devices"]:
        if not device.get("battery_entity_id"):
            primary_device_id = entity_device_ids.get(
                device.get("primary_entity_id", ""), device.get("ha_device_id", "")
            )
            candidates = battery_by_device.get(primary_device_id, [])
            if len(candidates) == 1:
                device["battery_entity_id"] = candidates[0]
        entity_id = device.get("battery_entity_id", "")
        state = hass.states.get(entity_id) if entity_id else None
        device["battery_level"] = _battery_level(state)
        device["battery_available"] = bool(
            state is not None and state.state not in {"unknown", "unavailable"}
        )
        ha_device_id = _inventory_ha_device_id(device, entity_registry)
        device.update(
            firmware_updates.get(
                ha_device_id,
                {
                    "firmware_update_entity_id": "",
                    "firmware_update_disabled": False,
                    "firmware_update_available": False,
                    "firmware_update_in_progress": False,
                    "firmware_update_percentage": None,
                    "firmware_installed_version": "",
                    "firmware_latest_version": "",
                    "firmware_release_url": "",
                    "firmware_available": False,
                },
            )
        )
    data["areas"] = sorted(
        (area.name for area in ar.async_get(hass).async_list_areas()),
        key=str.casefold,
    )
    data["version"] = VERSION
    connection.send_result(msg["id"], data)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/add",
        vol.Required("device"): dict,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_add(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Add one device."""
    try:
        if not isinstance(msg.get("device"), dict):
            raise InventoryError("Device data is required")
        device = await _manager(hass).async_add(msg["device"])
        _push_device_labels_to_home_assistant(hass, device)
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_device", str(err))
        return
    connection.send_result(msg["id"], device)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/update",
        vol.Required("device_id"): str,
        vol.Required("device"): dict,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_update(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Update one device."""
    try:
        if not isinstance(msg.get("device_id"), str) or not isinstance(
            msg.get("device"), dict
        ):
            raise InventoryError("Device ID and device data are required")
        device = await _manager(hass).async_update(msg["device_id"], msg["device"])
        _push_device_labels_to_home_assistant(hass, device)
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_device", str(err))
        return
    connection.send_result(msg["id"], device)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/battery_replaced",
        vol.Required("device_id"): str,
        vol.Required("replaced_at"): str,
        vol.Optional("note", default=""): str,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_battery_replaced(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Record a battery replacement for one inventory device."""
    try:
        device = await _manager(hass).async_record_battery_replacement(
            msg["device_id"], msg["replaced_at"], msg["note"]
        )
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_battery_replacement", str(err))
        return
    connection.send_result(msg["id"], device)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/bulk_update",
        vol.Required("device_ids"): [str],
        vol.Required("fields"): dict,
        vol.Optional("label_mode", default=""): str,
        vol.Optional("labels", default=[]): [str],
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_bulk_update(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Update selected fields on multiple inventory devices."""
    try:
        result = await _manager(hass).async_bulk_update(
            msg["device_ids"], msg["fields"], msg["label_mode"], msg["labels"]
        )
        data = await _manager(hass).async_snapshot()
        for device in data["devices"]:
            if device["id"] in msg["device_ids"]:
                _push_device_labels_to_home_assistant(hass, device)
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_bulk_update", str(err))
        return
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/delete",
        vol.Required("device_id"): str,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_delete(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Delete one device."""
    try:
        if not isinstance(msg.get("device_id"), str):
            raise InventoryError("Device ID is required")
        await _manager(hass).async_delete(msg["device_id"])
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_device", str(err))
        return
    connection.send_result(msg["id"], {})


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/import",
        vol.Required("devices"): [dict],
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_import(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Import devices from CSV or the HA registry."""
    try:
        if not isinstance(msg.get("devices"), list) or not all(
            isinstance(item, dict) for item in msg["devices"]
        ):
            raise InventoryError("A device list is required")
        result = await _manager(hass).async_import(msg["devices"])
        data = await _manager(hass).async_snapshot()
        for device in data["devices"]:
            _push_device_labels_to_home_assistant(hass, device)
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_import", str(err))
        return
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({"type": f"{DOMAIN}/export"})
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_export(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Export a portable JSON backup."""
    connection.send_result(msg["id"], await _manager(hass).async_export())


@websocket_api.websocket_command(
    {"type": f"{DOMAIN}/restore", vol.Required("backup"): dict}
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_restore(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Restore a portable JSON backup."""
    try:
        result = await _manager(hass).async_restore(msg["backup"])
        for device in result["devices"]:
            _push_device_labels_to_home_assistant(hass, device)
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_backup", str(err))
        return
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command(
    {"type": f"{DOMAIN}/restore_backup", vol.Required("backup_id"): str}
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_restore_backup(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Restore an automatic backup."""
    try:
        result = await _manager(hass).async_restore_backup(msg["backup_id"])
        for device in result["devices"]:
            _push_device_labels_to_home_assistant(hass, device)
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_backup", str(err))
        return
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/unifi/connect",
        vol.Optional("api_key"): str,
        vol.Optional("host_id", default=""): str,
        vol.Optional("site_id", default=""): str,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_unifi_connect(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Validate UniFi Cloud credentials and select a site."""
    try:
        result = await _unifi(hass).async_connect(
            msg.get("api_key"), msg.get("host_id", ""), msg.get("site_id", "")
        )
    except UniFiError as err:
        connection.send_error(msg["id"], "unifi_error", str(err))
        return
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command({"type": f"{DOMAIN}/unifi/disconnect"})
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_unifi_disconnect(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Disconnect UniFi Cloud and erase its API key."""
    await _unifi(hass).async_disconnect()
    connection.send_result(msg["id"], {})


@websocket_api.websocket_command({"type": f"{DOMAIN}/unifi/refresh"})
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_unifi_refresh(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Refresh clients and infrastructure from UniFi Cloud."""
    try:
        await _unifi(hass).async_refresh()
    except UniFiError as err:
        connection.send_error(msg["id"], "unifi_error", str(err))
        return
    connection.send_result(msg["id"], _unifi(hass).status())


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/niimbot/configure",
        vol.Required("device_id"): str,
        vol.Required("label_width_mm"): vol.Coerce(float),
        vol.Required("label_height_mm"): vol.Coerce(float),
        vol.Required("margin_mm"): vol.Coerce(float),
        vol.Required("top_margin_mm"): vol.Coerce(float),
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_niimbot_configure(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Select the Home Assistant NIIMBOT printer."""
    printers = {item["device_id"] for item in _niimbot_printers(hass)}
    if msg["device_id"] not in printers:
        connection.send_error(msg["id"], "niimbot_error", "NIIMBOT printer not found")
        return
    width = msg["label_width_mm"]
    height = msg["label_height_mm"]
    margin = msg["margin_mm"]
    top_margin = msg["top_margin_mm"]
    if not 20 <= width <= 200 or not 8 <= height <= 15:
        connection.send_error(msg["id"], "niimbot_error", "D11H label size must be 20–200 × 8–15 mm")
        return
    if not 0.5 <= margin <= 3 or margin * 2 >= height:
        connection.send_error(msg["id"], "niimbot_error", "Label margin must be between 0.5 and 3 mm")
        return
    if not 0.5 <= top_margin <= 4 or top_margin + margin >= height:
        connection.send_error(msg["id"], "niimbot_error", "Top margin must be between 0.5 and 4 mm")
        return
    result = await _manager(hass).async_save_niimbot(
        msg["device_id"], width, height, margin, top_margin
    )
    connection.send_result(msg["id"], result)


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/niimbot/print",
        vol.Required("device_id"): str,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_niimbot_print(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Print a temporary D11H inventory label."""
    data = await _manager(hass).async_snapshot()
    settings = data.get("niimbot", {})
    printer_id = str(settings.get("device_id") or "")
    device = next(
        (item for item in data["devices"] if item["id"] == msg["device_id"]),
        None,
    )
    if not printer_id or printer_id not in {
        item["device_id"] for item in _niimbot_printers(hass)
    }:
        connection.send_error(msg["id"], "niimbot_error", "Select a NIIMBOT printer first")
        return
    if device is None:
        connection.send_error(msg["id"], "niimbot_error", "Inventory device not found")
        return
    if not hass.services.has_service("niimbot", "print"):
        connection.send_error(msg["id"], "niimbot_error", "NIIMBOT print service is unavailable")
        return

    pixels_per_mm = 300 / 25.4
    width = round(float(settings["label_width_mm"]) * pixels_per_mm)
    height = round(float(settings["label_height_mm"]) * pixels_per_mm)
    margin = round(float(settings["margin_mm"]) * pixels_per_mm)
    content_y = round(float(settings["top_margin_mm"]) * pixels_per_mm)
    content_width = width - (margin * 2)
    content_height = height - content_y - margin
    name_height = round(content_height * 0.48)
    detail_height = round(content_height * 0.26)
    protocol = data["protocols"].get(device["protocol"], {}).get(
        "label", device["protocol"]
    )
    service_data = {
        "payload": [
            {
                "type": "new_multiline",
                "value": device["name"],
                "x": margin,
                "y": content_y,
                "width": content_width,
                "height": name_height,
                "size": 38,
                "fit": True,
            },
            {
                "type": "text",
                "value": f"ID {device['device_code']}  |  {protocol}",
                "x": margin,
                "y": content_y + name_height,
                "size": 27,
            },
            {
                "type": "text",
                "value": device["mac"],
                "x": margin,
                "y": content_y + name_height + detail_height,
                "size": 25,
            },
        ],
        "rotate": 90,
        "width": width,
        "height": height,
        "density": 3,
        "label_type": 1,
        "copies": 1,
    }
    try:
        await hass.services.async_call(
            "niimbot",
            "print",
            service_data,
            blocking=True,
            target={"device_id": printer_id},
        )
    except HomeAssistantError as err:
        connection.send_error(msg["id"], "niimbot_error", str(err))
        return
    connection.send_result(msg["id"], {"printed": True})


@websocket_api.websocket_command(
    {
        vol.Required("type"): f"{DOMAIN}/settings",
        vol.Required("settings"): dict,
    }
)
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_settings(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Update protocol ranges and device types."""
    try:
        if not isinstance(msg.get("settings"), dict):
            raise InventoryError("Settings data is required")
        settings = dict(msg["settings"])
        _ensure_home_assistant_labels(hass, settings.get("labels", []))
        settings["labels"] = _home_assistant_label_names(hass)
        result = await _manager(hass).async_save_settings(settings)
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_settings", str(err))
        return
    connection.send_result(msg["id"], result)


@callback
def _ensure_home_assistant_labels(
    hass: HomeAssistant, names: list[str]
) -> dict[str, str]:
    """Create missing Home Assistant labels and return name-to-ID mapping."""
    registry = lr.async_get(hass)
    for name in sorted(
        {str(item).strip()[:60] for item in names if str(item).strip()},
        key=str.casefold,
    ):
        if registry.async_get_label_by_name(name) is None:
            registry.async_create(name)
    return {
        item.name.casefold(): item.label_id for item in registry.async_list_labels()
    }


@callback
def _home_assistant_label_names(hass: HomeAssistant) -> list[str]:
    """Return every Home Assistant label name."""
    return sorted(
        (item.name for item in lr.async_get(hass).async_list_labels()),
        key=str.casefold,
    )


@callback
def _inventory_label_target(
    hass: HomeAssistant, device: dict[str, Any]
) -> tuple[str, Any] | None:
    """Resolve an inventory item to its Home Assistant device or entity."""
    entity_registry = er.async_get(hass)
    primary_entity = entity_registry.async_get(device.get("primary_entity_id", ""))
    device_ids = [device.get("ha_device_id")]
    if primary_entity:
        device_ids.append(primary_entity.device_id)
    device_registry = dr.async_get(hass)
    for device_id in device_ids:
        if device_id and (ha_device := device_registry.async_get(device_id)):
            return "device", ha_device
    if primary_entity:
        return "entity", primary_entity
    return None


@callback
def _push_device_labels_to_home_assistant(
    hass: HomeAssistant, device: dict[str, Any], *, merge: bool = False
) -> bool:
    """Apply one inventory item's labels to its matching HA registry entry."""
    label_ids_by_name = _ensure_home_assistant_labels(
        hass, device.get("labels", [])
    )
    target = _inventory_label_target(hass, device)
    if target is None:
        return False
    label_ids = {
        label_ids_by_name[name.casefold()]
        for name in device.get("labels", [])
        if name.casefold() in label_ids_by_name
    }
    target_type, entry = target
    if merge:
        label_ids.update(entry.labels)
    if entry.labels == label_ids:
        return True
    if target_type == "device":
        dr.async_get(hass).async_update_device(entry.id, labels=label_ids)
    else:
        er.async_get(hass).async_update_entity(entry.entity_id, labels=label_ids)
    return True


async def async_sync_labels_from_home_assistant(hass: HomeAssistant) -> None:
    """Synchronize HA labels and assignments into persistent inventory data."""
    manager = _manager(hass)
    data = await manager.async_snapshot()
    if not data.get("ha_labels_migrated"):
        _ensure_home_assistant_labels(hass, data.get("labels", []))
        for device in data["devices"]:
            _push_device_labels_to_home_assistant(hass, device, merge=True)

    labels_by_id = {
        item.label_id: item.name
        for item in lr.async_get(hass).async_list_labels()
    }
    device_labels: dict[str, list[str]] = {}
    for device in data["devices"]:
        target = _inventory_label_target(hass, device)
        if target is None:
            continue
        _, entry = target
        device_labels[device["id"]] = sorted(
            (labels_by_id[label_id] for label_id in entry.labels if label_id in labels_by_id),
            key=str.casefold,
        )
    await manager.async_sync_ha_labels(
        sorted(labels_by_id.values(), key=str.casefold), device_labels
    )


@callback
def _home_assistant_entities(hass: HomeAssistant) -> list[dict[str, str]]:
    """Return searchable Home Assistant entities and their device relationship."""
    entity_registry = er.async_get(hass)
    result: list[dict[str, str]] = []
    for state in hass.states.async_all():
        registry_entry = entity_registry.async_get(state.entity_id)
        result.append(
            {
                "entity_id": state.entity_id,
                "name": str(state.attributes.get("friendly_name", state.entity_id)),
                "device_id": registry_entry.device_id if registry_entry else "",
            }
        )
    return sorted(result, key=lambda item: (item["name"].casefold(), item["entity_id"]))


@callback
def _battery_entities(hass: HomeAssistant) -> list[dict[str, Any]]:
    """Return Home Assistant sensors that expose a battery percentage."""
    entity_registry = er.async_get(hass)
    result: list[dict[str, Any]] = []
    for state in hass.states.async_all("sensor"):
        device_class = str(state.attributes.get("device_class", ""))
        unit = str(state.attributes.get("unit_of_measurement", ""))
        friendly_name = str(state.attributes.get("friendly_name", state.entity_id))
        searchable = f"{state.entity_id} {friendly_name}".casefold()
        if device_class != "battery" and not (unit == "%" and "battery" in searchable):
            continue
        registry_entry = entity_registry.async_get(state.entity_id)
        result.append(
            {
                "entity_id": state.entity_id,
                "name": friendly_name,
                "level": _battery_level(state),
                "available": state.state not in {"unknown", "unavailable"},
                "device_id": registry_entry.device_id if registry_entry else "",
            }
        )
    return sorted(result, key=lambda item: (item["name"].casefold(), item["entity_id"]))


def _battery_level(state: Any) -> float | int | None:
    """Return a clamped battery percentage from a Home Assistant state."""
    if state is None or state.state in {"unknown", "unavailable"}:
        return None
    try:
        level = max(0.0, min(100.0, float(state.state)))
    except (TypeError, ValueError):
        return None
    return int(level) if level.is_integer() else round(level, 1)


@callback
def _inventory_ha_device_id(device: dict[str, Any], registry: Any) -> str:
    """Resolve the Home Assistant device linked to an inventory item."""
    primary_entity = registry.async_get(device.get("primary_entity_id", ""))
    if primary_entity and primary_entity.device_id:
        return primary_entity.device_id
    return str(device.get("ha_device_id") or "")


@callback
def _shelly_firmware_updates(hass: HomeAssistant) -> dict[str, dict[str, Any]]:
    """Return the stable Shelly firmware update entity for each HA device."""
    registry = er.async_get(hass)
    updates = {}
    for device_id, entry in select_shelly_firmware_entries(
        registry.entities.values()
    ).items():
        state = hass.states.get(entry.entity_id)
        updates[device_id] = firmware_update_details(entry, state)
    return updates


@callback
def _home_assistant_devices(
    hass: HomeAssistant, inventory_devices: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Build a serialisable list from Home Assistant's device registry."""
    device_registry = dr.async_get(hass)
    area_registry = ar.async_get(hass)
    entity_registry = er.async_get(hass)
    labels_by_id = {
        item.label_id: item.name
        for item in lr.async_get(hass).async_list_labels()
    }
    imported_ids = {
        item.get("ha_device_id") for item in inventory_devices if item.get("ha_device_id")
    }
    result: list[dict[str, Any]] = []

    registry_devices = [*device_registry.devices, *device_registry.child_devices]
    for device in registry_devices:
        if device.id in imported_ids:
            continue
        config_entry = hass.config_entries.async_get_entry(device.config_entry_id)
        domains = [config_entry.domain] if config_entry is not None else []
        is_child = isinstance(device, dr.ChildDeviceEntry)
        parent = (
            device_registry.async_get(
                device.parent_device_id,
                include_child_devices=False,
                include_composite_devices=False,
            )
            if is_child
            else None
        )
        connections = (
            {} if is_child else {kind: value for kind, value in device.connections}
        )
        entities = [
            entry
            for entry in entity_registry.entities.values()
            if entry.device_id == device.id
        ]
        entity_ids = sorted(entry.entity_id for entry in entities)
        primary_entity_id = _primary_entity_id(hass, entities)
        area_id = device.area_id or (parent.area_id if parent else None) or next(
            (entry.area_id for entry in entities if entry.area_id), None
        )
        area = area_registry.async_get_area(area_id) if area_id else None
        device_name = device.name_by_user or device.name
        if not device_name:
            device_name = (
                parent.model
                if is_child and parent
                else ""
                if is_child
                else device.model
            )
        brand = (
            parent.manufacturer
            if is_child and parent
            else "" if is_child else device.manufacturer
        ) or (domains[0].replace("_", " ").title() if domains else "Home Assistant")
        result.append(
            {
                "ha_device_id": device.id,
                "name": device_name or "Unnamed device",
                "brand": brand,
                "model": (
                    parent.model
                    if is_child and parent
                    else ""
                    if is_child
                    else device.model
                )
                or "",
                "area": area.name if area else "",
                "mac": _hardware_address(connections),
                "ip_address": "" if is_child else _configuration_ip(device.configuration_url),
                "device_type": _guess_device_type(entity_ids),
                "protocol": _guess_protocol(domains),
                "integration": ", ".join(domains),
                "device_identifier": _first_identifier(device.identifiers),
                "entity_name": common_entity_name(entity_ids),
                "primary_entity_id": primary_entity_id,
                "status": "unknown",
                "labels": sorted(
                    (
                        labels_by_id[label_id]
                        for label_id in device.labels
                        if label_id in labels_by_id
                    ),
                    key=str.casefold,
                ),
                "ha_device_kind": "child" if is_child else "device",
                "parent_ha_device_id": device.parent_device_id if is_child else "",
                "parent_device_name": (
                    parent.name_by_user or parent.name or parent.model or ""
                    if parent
                    else ""
                ),
                "ha_config_entry_id": device.config_entry_id,
                "ha_config_subentry_id": device.config_subentry_id or "",
            }
        )

    return sorted(result, key=lambda item: item["name"].casefold())


def _primary_entity_id(hass: HomeAssistant, entities: list[Any]) -> str:
    """Choose a useful default primary entity without selecting a battery sensor."""
    if not entities:
        return ""

    def priority(entry: Any) -> tuple[bool, bool, bool, str]:
        state = hass.states.get(entry.entity_id)
        is_battery = bool(
            state and str(state.attributes.get("device_class", "")) == "battery"
        )
        return (
            is_battery,
            entry.entity_category is not None,
            entry.disabled_by is not None,
            entry.entity_id,
        )

    return min(entities, key=priority).entity_id


def _guess_protocol(domains: list[str]) -> str:
    domain_set = set(domains)
    if "zha" in domain_set:
        return "zigbee"
    if "bluetooth" in domain_set:
        return "bluetooth"
    if "matter" in domain_set:
        return "matter"
    if "zwave_js" in domain_set:
        return "zwave"
    if domain_set & {
        "esphome",
        "homekit_controller",
        "shelly",
        "tplink",
        "tuya",
        "wiz",
    }:
        return "wifi"
    return "other"


def _hardware_address(connections: dict[str, str]) -> str:
    """Return the available MAC, Zigbee IEEE, or Bluetooth address."""
    return (
        connections.get(dr.CONNECTION_NETWORK_MAC)
        or connections.get(dr.CONNECTION_ZIGBEE)
        or connections.get(dr.CONNECTION_BLUETOOTH)
        or ""
    )


def _configuration_ip(configuration_url: Any) -> str:
    """Return an IP address from a device configuration URL."""
    if not configuration_url:
        return ""
    host = urlparse(str(configuration_url)).hostname
    if not host:
        return ""
    try:
        ip_address(host)
    except ValueError:
        return ""
    return host


def _guess_device_type(entity_ids: list[str]) -> str:
    """Infer an inventory type from the device's entity domains."""
    domains = {entity_id.partition(".")[0] for entity_id in entity_ids}
    for domain, device_type in (
        ("camera", "Camera"),
        ("vacuum", "Vacuum"),
        ("humidifier", "Humidifier"),
        ("fan", "Fan"),
        ("light", "Light"),
        ("lock", "Lock"),
        ("siren", "Siren"),
        ("valve", "Valve"),
        ("switch", "Switch"),
        ("climate", "Thermostat"),
        ("media_player", "Media Player"),
        ("sensor", "Sensor"),
        ("binary_sensor", "Sensor"),
    ):
        if domain in domains:
            return device_type
    return ""


def _first_identifier(identifiers: set[tuple[str, str]]) -> str:
    if not identifiers:
        return ""
    domain, identifier = sorted(identifiers)[0]
    return f"{domain}:{identifier}"
