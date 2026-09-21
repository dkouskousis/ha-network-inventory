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


def device_payload(name, protocol, **values):
    payload = {
        "name": name,
        "device_type": "Sensor",
        "brand": "Test Brand",
        "area": "Test Area",
        "protocol": protocol,
        "mac": "00:11:22:33:44:55",
    }
    if protocol.lower().replace("-", "_") in {"wifi", "wi_fi", "ethernet"}:
        payload["ip_address"] = "192.168.1.10"
    payload.update(values)
    return payload


class DeviceIdTests(unittest.IsolatedAsyncioTestCase):
    async def asyncSetUp(self):
        self.manager = storage.InventoryStore(None)
        await self.manager.async_load()

    async def test_default_protocol_ranges(self):
        wifi = await self.manager.async_add(device_payload("Router", "Wi-Fi"))
        zigbee = await self.manager.async_add(device_payload("Motion", "ZigBee"))
        bluetooth = await self.manager.async_add(
            device_payload("Thermometer", "Bluetooth")
        )
        self.assertEqual(wifi["device_code"], 1001)
        self.assertEqual(zigbee["device_code"], 2001)
        self.assertEqual(bluetooth["device_code"], 3001)

    async def test_id_is_stable_and_never_reused(self):
        first = await self.manager.async_add(device_payload("One", "wifi"))
        changed = await self.manager.async_update(
            first["id"], {"protocol": "zigbee"}
        )
        self.assertEqual(changed["device_code"], 1001)
        await self.manager.async_delete(first["id"])
        second = await self.manager.async_add(device_payload("Two", "wifi"))
        self.assertEqual(second["device_code"], 1002)

    async def test_clearing_id_assigns_next_id_for_new_protocol(self):
        first = await self.manager.async_add(device_payload("Plug", "wifi"))
        changed = await self.manager.async_update(
            first["id"], {"protocol": "zigbee", "device_code": ""}
        )
        self.assertEqual(first["device_code"], 1001)
        self.assertEqual(changed["device_code"], 2001)

        next_wifi = await self.manager.async_add(device_payload("Router", "wifi"))
        next_zigbee = await self.manager.async_add(
            device_payload("Sensor", "zigbee")
        )
        self.assertEqual(next_wifi["device_code"], 1002)
        self.assertEqual(next_zigbee["device_code"], 2002)

    async def test_extended_device_types_are_available(self):
        for device_type in ("Vacuum", "Humidifier", "Printer", "Relay", "Plug"):
            self.assertIn(device_type, self.manager.data["device_types"])

    async def test_import_preserves_excel_code_and_advances_counter(self):
        result = await self.manager.async_import(
            [device_payload("Existing sensor", "zigbee", device_code=2014)]
        )
        new_device = await self.manager.async_add(
            device_payload("New sensor", "zigbee")
        )
        self.assertEqual(result["imported"], 1)
        self.assertEqual(new_device["device_code"], 2015)

    async def test_entity_name_is_stored_and_updated(self):
        device = await self.manager.async_import(
            [
                device_payload("Shelly lamp", "wifi", entity_name="lamp")
            ]
        )
        self.assertEqual(device["imported"], 1)
        stored = self.manager.data["devices"][0]
        self.assertEqual(stored["entity_name"], "lamp")

        updated = await self.manager.async_update(
            stored["id"], {"entity_name": "living_room_lamp"}
        )
        self.assertEqual(updated["entity_name"], "living_room_lamp")

    async def test_import_adds_new_brand_to_settings(self):
        await self.manager.async_import(
            [device_payload("Imported", "zigbee", brand="Imported Brand")]
        )
        self.assertIn("Imported Brand", self.manager.data["brands"])

    async def test_niimbot_printer_selection_is_stored(self):
        result = await self.manager.async_save_niimbot("printer-device-id", 40, 15, 1.5, 2)
        self.assertEqual(result["device_id"], "printer-device-id")
        self.assertEqual(result["label_width_mm"], 40)
        self.assertEqual(result["top_margin_mm"], 2)
        self.assertEqual(self.manager.data["niimbot"]["device_id"], "printer-device-id")

    async def test_required_fields_and_ip_validation(self):
        with self.assertRaisesRegex(storage.InventoryError, "Type"):
            await self.manager.async_add(
                device_payload("Incomplete", "zigbee", device_type="")
            )
        with self.assertRaisesRegex(storage.InventoryError, "IP address"):
            await self.manager.async_add(
                device_payload("No IP", "wifi", ip_address="")
            )

    def test_common_entity_name(self):
        self.assertEqual(
            storage.common_entity_name(
                [
                    "light.lamp_10",
                    "sensor.lamp_10_power",
                    "sensor.lamp_10_temperature",
                ]
            ),
            "lamp_10",
        )


if __name__ == "__main__":
    unittest.main()
