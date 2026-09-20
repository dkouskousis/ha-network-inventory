"""Tests for permanent protocol-based Device IDs."""

from __future__ import annotations

import importlib.util
from pathlib import Path
import sys
import types
import unittest


class DummyStore:
    """Minimal Home Assistant Store replacement."""

    def __class_getitem__(cls, item):
        return cls

    def __init__(self, *args, **kwargs):
        self.saved = None

    async def async_load(self):
        return None

    async def async_save(self, data):
        self.saved = data


def load_storage_module():
    """Load the storage module without installing Home Assistant."""
    root = Path(__file__).parents[1] / "custom_components" / "network_inventory"
    homeassistant = types.ModuleType("homeassistant")
    core = types.ModuleType("homeassistant.core")
    helpers = types.ModuleType("homeassistant.helpers")
    storage_stub = types.ModuleType("homeassistant.helpers.storage")
    core.HomeAssistant = object
    storage_stub.Store = DummyStore
    sys.modules.update(
        {
            "homeassistant": homeassistant,
            "homeassistant.core": core,
            "homeassistant.helpers": helpers,
            "homeassistant.helpers.storage": storage_stub,
        }
    )
    package = types.ModuleType("network_inventory")
    package.__path__ = [str(root)]
    sys.modules["network_inventory"] = package
    for name in ("const", "storage"):
        spec = importlib.util.spec_from_file_location(
            f"network_inventory.{name}", root / f"{name}.py"
        )
        module = importlib.util.module_from_spec(spec)
        sys.modules[f"network_inventory.{name}"] = module
        spec.loader.exec_module(module)
    return sys.modules["network_inventory.storage"]


storage = load_storage_module()


class DeviceIdTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.manager = storage.InventoryStore(None)
        await self.manager.async_load()

    async def test_default_protocol_ranges(self):
        wifi = await self.manager.async_add({"name": "Router", "protocol": "Wi-Fi"})
        zigbee = await self.manager.async_add({"name": "Motion", "protocol": "ZigBee"})
        bluetooth = await self.manager.async_add(
            {"name": "Thermometer", "protocol": "Bluetooth"}
        )
        self.assertEqual(wifi["device_code"], 1001)
        self.assertEqual(zigbee["device_code"], 2001)
        self.assertEqual(bluetooth["device_code"], 3001)

    async def test_id_is_stable_and_never_reused(self):
        first = await self.manager.async_add({"name": "One", "protocol": "wifi"})
        changed = await self.manager.async_update(
            first["id"], {"protocol": "zigbee"}
        )
        self.assertEqual(changed["device_code"], 1001)
        await self.manager.async_delete(first["id"])
        second = await self.manager.async_add({"name": "Two", "protocol": "wifi"})
        self.assertEqual(second["device_code"], 1002)

    async def test_import_preserves_excel_code_and_advances_counter(self):
        result = await self.manager.async_import(
            [{"name": "Existing sensor", "protocol": "zigbee", "device_code": 2014}]
        )
        new_device = await self.manager.async_add(
            {"name": "New sensor", "protocol": "zigbee"}
        )
        self.assertEqual(result["imported"], 1)
        self.assertEqual(new_device["device_code"], 2015)

    async def test_entity_id_is_stored_and_updated(self):
        device = await self.manager.async_import(
            [
                {
                    "name": "Shelly lamp",
                    "protocol": "wifi",
                    "entity_id": "light.lamp, sensor.lamp_power",
                }
            ]
        )
        self.assertEqual(device["imported"], 1)
        stored = self.manager.data["devices"][0]
        self.assertEqual(stored["entity_id"], "light.lamp, sensor.lamp_power")

        updated = await self.manager.async_update(
            stored["id"], {"entity_id": "light.lamp"}
        )
        self.assertEqual(updated["entity_id"], "light.lamp")


if __name__ == "__main__":
    unittest.main()
