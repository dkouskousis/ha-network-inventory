"""Tests for UniFi matching and data transformation."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import types
import unittest


def load_unifi_module():
    root = Path(__file__).parents[1] / "custom_components" / "network_inventory"
    homeassistant = sys.modules.get("homeassistant") or types.ModuleType("homeassistant")
    core = sys.modules.get("homeassistant.core") or types.ModuleType("homeassistant.core")
    helpers = sys.modules.get("homeassistant.helpers") or types.ModuleType("homeassistant.helpers")
    aiohttp_client = types.ModuleType("homeassistant.helpers.aiohttp_client")
    storage = sys.modules.get("homeassistant.helpers.storage") or types.ModuleType("homeassistant.helpers.storage")
    core.HomeAssistant = object
    aiohttp_client.async_get_clientsession = lambda hass: None
    if not hasattr(storage, "Store"):
        storage.Store = object
    sys.modules.update(
        {
            "homeassistant": homeassistant,
            "homeassistant.core": core,
            "homeassistant.helpers": helpers,
            "homeassistant.helpers.aiohttp_client": aiohttp_client,
            "homeassistant.helpers.storage": storage,
        }
    )
    package = sys.modules.get("network_inventory") or types.ModuleType("network_inventory")
    package.__path__ = [str(root)]
    sys.modules["network_inventory"] = package
    if "network_inventory.const" not in sys.modules:
        spec = importlib.util.spec_from_file_location("network_inventory.const", root / "const.py")
        const = importlib.util.module_from_spec(spec)
        sys.modules["network_inventory.const"] = const
        spec.loader.exec_module(const)
    spec = importlib.util.spec_from_file_location("network_inventory.unifi", root / "unifi.py")
    module = importlib.util.module_from_spec(spec)
    sys.modules["network_inventory.unifi"] = module
    spec.loader.exec_module(module)
    return module


unifi = load_unifi_module()


class UniFiTests(unittest.TestCase):
    def test_normalize_mac(self):
        self.assertEqual(unifi.normalize_mac("AA:BB:CC:DD:EE:FF"), "aabbccddeeff")
        self.assertEqual(unifi.normalize_mac("aa-bb-cc-dd-ee-ff"), "aabbccddeeff")
        self.assertEqual(unifi.normalize_mac("invalid"), "")

    def test_matches_inventory_without_mutating_items(self):
        devices = [{"id": "inventory-1", "mac": "AA:BB:CC:DD:EE:FF"}]
        items = [{"id": "client-1", "mac": "aa-bb-cc-dd-ee-ff", "name": "Laptop"}]
        matches, enriched = unifi.match_unifi_items(devices, items)
        self.assertEqual(matches["inventory-1"]["id"], "client-1")
        self.assertEqual(matches["inventory-1"]["inventory_id"], "inventory-1")
        self.assertEqual(enriched[0]["inventory_id"], "inventory-1")
        self.assertNotIn("inventory_id", items[0])

    def test_client_includes_uplink_details(self):
        client = {
            "id": "client-1", "name": "Phone", "type": "WIRELESS",
            "macAddress": "00:11:22:33:44:55", "ipAddress": "192.168.1.20",
            "uplinkDeviceId": "ap-1", "networkName": "IoT", "vlanId": 30,
            "ssid": "House IoT",
        }
        result = unifi.UniFiCloudManager._client_item(
            client, {"ap-1": {"name": "Living Room AP", "model": "U6-PRO"}}
        )
        self.assertEqual(result["protocol"], "wifi")
        self.assertEqual(result["uplink_name"], "Living Room AP")
        self.assertEqual(result["network"], "IoT")
        self.assertEqual(result["vlan"], "30")
        self.assertEqual(result["ssid"], "House IoT")

    def test_network_site_uuid_is_used_instead_of_site_manager_id(self):
        manager_sites = [
            {
                "siteId": "661de833b6b2463f0c20b319",
                "hostId": "console-1",
                "meta": {
                    "name": "default",
                    "desc": "Home",
                    "gatewayMac": "00:11:22:33:44:55",
                },
            }
        ]
        network_site = {
            "id": "210c0702-6f1c-40a5-a2ac-46c4c1ca1285",
            "internalReference": "default",
            "name": "Default",
        }
        result = unifi.UniFiCloudManager._network_site_choice(
            "console-1", network_site, manager_sites
        )
        self.assertEqual(result["site_id"], network_site["id"])
        self.assertEqual(result["name"], "Home")

    def test_site_manager_choice_does_not_contact_console(self):
        choice = unifi.UniFiCloudManager._manager_site_choice(
            {
                "siteId": "661de833b6b2463f0c20b319",
                "hostId": "console-1",
                "meta": {"name": "default", "desc": "Home"},
            }
        )
        self.assertEqual(choice["host_id"], "console-1")
        self.assertEqual(choice["site_id"], "661de833b6b2463f0c20b319")
        self.assertEqual(choice["name"], "Home")


if __name__ == "__main__":
    unittest.main()
