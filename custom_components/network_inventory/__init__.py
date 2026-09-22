"""Network Inventory integration."""

from __future__ import annotations

from pathlib import Path

from homeassistant.components import frontend, panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.helpers import device_registry as dr
from homeassistant.helpers import entity_registry as er
from homeassistant.helpers import label_registry as lr

from .const import DOMAIN, NAME, PANEL_URL
from .storage import InventoryStore
from .unifi import UniFiCloudManager
from .websocket import async_register_commands, async_sync_labels_from_home_assistant


async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Set up Network Inventory."""
    manager = InventoryStore(hass)
    await manager.async_load()
    domain_data = hass.data.setdefault(DOMAIN, {})
    domain_data["manager"] = manager
    unifi = UniFiCloudManager(hass)
    await unifi.async_load()
    domain_data["unifi"] = unifi

    if not domain_data.get("static_registered"):
        frontend_dir = Path(__file__).parent / "frontend"
        await hass.http.async_register_static_paths(
            [StaticPathConfig(PANEL_URL, str(frontend_dir), cache_headers=False)]
        )
        domain_data["static_registered"] = True
    if not domain_data.get("commands_registered"):
        async_register_commands(hass)
        domain_data["commands_registered"] = True
    if not domain_data.get("label_sync_unsubs"):
        async def _registry_updated(event) -> None:
            if not manager.data.get("ha_labels_migrated"):
                return
            if event.event_type in {
                dr.EVENT_DEVICE_REGISTRY_UPDATED,
                er.EVENT_ENTITY_REGISTRY_UPDATED,
            } and event.data.get("action") == "update":
                if "labels" not in event.data.get("changes", {}):
                    return
            await async_sync_labels_from_home_assistant(hass)

        domain_data["label_sync_unsubs"] = [
            hass.bus.async_listen(lr.EVENT_LABEL_REGISTRY_UPDATED, _registry_updated),
            hass.bus.async_listen(dr.EVENT_DEVICE_REGISTRY_UPDATED, _registry_updated),
            hass.bus.async_listen(er.EVENT_ENTITY_REGISTRY_UPDATED, _registry_updated),
        ]
    if not domain_data.get("panel_registered"):
        await panel_custom.async_register_panel(
            hass=hass,
            frontend_url_path=DOMAIN,
            webcomponent_name="network-inventory-panel",
            sidebar_title=NAME,
            sidebar_icon="mdi:lan",
            module_url=f"{PANEL_URL}/network-inventory-panel.js?v=0.14.0",
            require_admin=True,
            handle_safe_area=True,
        )
        domain_data["panel_registered"] = True
    return True


async def async_unload_entry(hass: HomeAssistant, entry: ConfigEntry) -> bool:
    """Unload Network Inventory."""
    frontend.async_remove_panel(hass, DOMAIN)
    hass.data[DOMAIN].pop("manager", None)
    hass.data[DOMAIN].pop("unifi", None)
    for unsubscribe in hass.data[DOMAIN].pop("label_sync_unsubs", []):
        unsubscribe()
    hass.data[DOMAIN]["panel_registered"] = False
    return True
