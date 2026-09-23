"""Tests for native firmware update discovery."""

from __future__ import annotations

from dataclasses import dataclass
import importlib.util
from pathlib import Path
import sys
import unittest


def load_firmware_module():
    path = (
        Path(__file__).parents[1]
        / "custom_components"
        / "network_inventory"
        / "firmware.py"
    )
    spec = importlib.util.spec_from_file_location("network_inventory_firmware", path)
    module = importlib.util.module_from_spec(spec)
    sys.modules[spec.name] = module
    spec.loader.exec_module(module)
    return module


firmware = load_firmware_module()


@dataclass
class Entry:
    entity_id: str
    device_id: str
    platform: str = "shelly"
    translation_key: str | None = None
    disabled_by: str | None = None


@dataclass
class State:
    state: str
    attributes: dict


class FirmwareTests(unittest.TestCase):
    def test_selects_stable_shelly_update_per_device(self):
        entries = [
            Entry("update.kitchen_beta", "device-1", translation_key="beta_firmware"),
            Entry("update.kitchen_firmware", "device-1"),
            Entry("update.router", "device-2", platform="unifi"),
            Entry("sensor.kitchen_version", "device-1"),
        ]
        selected = firmware.select_shelly_firmware_entries(entries)
        self.assertEqual(list(selected), ["device-1"])
        self.assertEqual(selected["device-1"].entity_id, "update.kitchen_firmware")

    def test_prefers_enabled_stable_entity(self):
        entries = [
            Entry("update.disabled_firmware", "device-1", disabled_by="integration"),
            Entry("update.enabled_firmware", "device-1"),
        ]
        selected = firmware.select_shelly_firmware_entries(entries)
        self.assertEqual(selected["device-1"].entity_id, "update.enabled_firmware")

    def test_selects_reolink_update_per_device(self):
        entries = [
            Entry("update.front_camera_firmware", "device-1", platform="reolink"),
            Entry("update.kitchen_firmware", "device-2"),
            Entry("sensor.front_camera_firmware", "device-1", platform="reolink"),
        ]
        selected = firmware.select_reolink_firmware_entries(entries)
        self.assertEqual(list(selected), ["device-1"])
        self.assertEqual(
            selected["device-1"].entity_id, "update.front_camera_firmware"
        )

    def test_builds_available_update_details(self):
        entry = Entry("update.living_room_firmware", "device-1")
        state = State(
            "on",
            {
                "installed_version": "1.5.0",
                "latest_version": "1.6.2",
                "release_url": "https://example.com/release",
                "in_progress": False,
            },
        )
        details = firmware.firmware_update_details(entry, state)
        self.assertTrue(details["firmware_update_available"])
        self.assertTrue(details["firmware_available"])
        self.assertEqual(details["firmware_installed_version"], "1.5.0")
        self.assertEqual(details["firmware_latest_version"], "1.6.2")
        self.assertEqual(details["firmware_integration"], "shelly")

    def test_uses_numeric_progress(self):
        entry = Entry("update.office_firmware", "device-1")
        state = State("on", {"in_progress": 42})
        details = firmware.firmware_update_details(entry, state)
        self.assertTrue(details["firmware_update_in_progress"])
        self.assertEqual(details["firmware_update_percentage"], 42)

    def test_summarizes_native_shelly_integration(self):
        updates = {
            "device-1": {
                "firmware_update_disabled": False,
                "firmware_update_available": True,
            },
            "device-2": {
                "firmware_update_disabled": True,
                "firmware_update_available": False,
            },
        }
        status = firmware.shelly_integration_status([object(), object()], updates)
        self.assertTrue(status["native"])
        self.assertTrue(status["configured"])
        self.assertEqual(status["device_count"], 2)
        self.assertEqual(status["firmware_entity_count"], 2)
        self.assertEqual(status["active_firmware_entity_count"], 1)
        self.assertEqual(status["updates_available"], 1)

    def test_summarizes_native_reolink_integration(self):
        updates = {
            "device-1": {
                "firmware_update_disabled": False,
                "firmware_update_available": True,
            }
        }
        status = firmware.reolink_integration_status(
            [object()], updates, device_count=4
        )
        self.assertTrue(status["native"])
        self.assertTrue(status["configured"])
        self.assertEqual(status["device_count"], 4)
        self.assertEqual(status["firmware_entity_count"], 1)
        self.assertEqual(status["active_firmware_entity_count"], 1)
        self.assertEqual(status["updates_available"], 1)


if __name__ == "__main__":
    unittest.main()
