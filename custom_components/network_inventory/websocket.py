"""WebSocket API for Network Inventory."""

from __future__ import annotations

from typing import Any

import voluptuous as vol

from homeassistant.components import websocket_api
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers import area_registry as ar
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er

from .const import DOMAIN
from .storage import InventoryError, InventoryStore, common_entity_name


def async_register_commands(hass: HomeAssistant) -> None:
    """Register the frontend API."""
    websocket_api.async_register_command(hass, websocket_list)
    websocket_api.async_register_command(hass, websocket_add)
    websocket_api.async_register_command(hass, websocket_update)
    websocket_api.async_register_command(hass, websocket_delete)
    websocket_api.async_register_command(hass, websocket_import)
    websocket_api.async_register_command(hass, websocket_settings)


def _manager(hass: HomeAssistant) -> InventoryStore:
    return hass.data[DOMAIN]["manager"]


@websocket_api.websocket_command({"type": f"{DOMAIN}/list"})
@websocket_api.require_admin
@websocket_api.async_response
async def websocket_list(
    hass: HomeAssistant,
    connection: websocket_api.ActiveConnection,
    msg: dict[str, Any],
) -> None:
    """Return inventory data and importable HA devices."""
    data = await _manager(hass).async_snapshot()
    data["ha_devices"] = _home_assistant_devices(hass, data["devices"])
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
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_device", str(err))
        return
    connection.send_result(msg["id"], device)


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
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_import", str(err))
        return
    connection.send_result(msg["id"], result)


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
        result = await _manager(hass).async_save_settings(msg["settings"])
    except InventoryError as err:
        connection.send_error(msg["id"], "invalid_settings", str(err))
        return
    connection.send_result(msg["id"], result)


@callback
def _home_assistant_devices(
    hass: HomeAssistant, inventory_devices: list[dict[str, Any]]
) -> list[dict[str, Any]]:
    """Build a serialisable list from Home Assistant's device registry."""
    device_registry = dr.async_get(hass)
    area_registry = ar.async_get(hass)
    entity_registry = er.async_get(hass)
    imported_ids = {
        item.get("ha_device_id") for item in inventory_devices if item.get("ha_device_id")
    }
    result: list[dict[str, Any]] = []

    for device in device_registry.devices.values():
        if device.id in imported_ids:
            continue
        domains = sorted(
            {
                entry.domain
                for entry_id in device.config_entries
                if (entry := hass.config_entries.async_get_entry(entry_id)) is not None
            }
        )
        connections = {kind: value for kind, value in device.connections}
        area = area_registry.async_get_area(device.area_id) if device.area_id else None
        entity_ids = sorted(
            entry.entity_id
            for entry in entity_registry.entities.values()
            if entry.device_id == device.id
        )
        result.append(
            {
                "ha_device_id": device.id,
                "name": device.name_by_user or device.name or device.model or "Unnamed device",
                "brand": device.manufacturer or "",
                "model": device.model or "",
                "area": area.name if area else "",
                "mac": connections.get(dr.CONNECTION_NETWORK_MAC, ""),
                "protocol": _guess_protocol(domains),
                "integration": ", ".join(domains),
                "device_identifier": _first_identifier(device.identifiers),
                "entity_name": common_entity_name(entity_ids),
                "status": "unknown",
            }
        )

    return sorted(result, key=lambda item: item["name"].casefold())


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


def _first_identifier(identifiers: set[tuple[str, str]]) -> str:
    if not identifiers:
        return ""
    domain, identifier = sorted(identifiers)[0]
    return f"{domain}:{identifier}"
