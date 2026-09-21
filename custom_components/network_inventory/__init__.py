"""Network Inventory integration."""

from __future__ import annotations

from pathlib import Path

from homeassistant.components import frontend, panel_custom
from homeassistant.components.http import StaticPathConfig
from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant

from .const import DOMAIN, NAME, PANEL_URL
from .storage import InventoryStore
from .unifi import UniFiCloudManager
from .websocket import async_register_commands


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
    if not domain_data.get("panel_registered"):
        await panel_custom.async_register_panel(
            hass=hass,
            frontend_url_path=DOMAIN,
            webcomponent_name="network-inventory-panel",
            sidebar_title=NAME,
            sidebar_icon="mdi:lan",
            module_url=f"{PANEL_URL}/network-inventory-panel.js?v=0.5.0",
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
    hass.data[DOMAIN]["panel_registered"] = False
    return True
