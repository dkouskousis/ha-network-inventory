"""Tests for permanent protocol-based Device IDs."""

from __future__ import annotations

import importlib.util
import json
from pathlib import Path
import sys
import types
import unittest
import tempfile
from io import BytesIO
from zipfile import ZipFile


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

files_spec = importlib.util.spec_from_file_location(
    "network_inventory.files",
    Path(__file__).parents[1]
    / "custom_components"
    / "network_inventory"
    / "files.py",
)
files = importlib.util.module_from_spec(files_spec)
sys.modules["network_inventory.files"] = files
files_spec.loader.exec_module(files)


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

    async def test_general_date_and_time_preferences_are_stored(self):
        self.assertEqual(
            self.manager.data["general"],
            {"time_format": "24h", "date_format": "day_first"},
        )
        result = await self.manager.async_save_settings(
            {"general": {"time_format": "12h", "date_format": "month_first"}}
        )
        self.assertEqual(
            result["general"],
            {"time_format": "12h", "date_format": "month_first"},
        )

    async def test_invalid_general_preferences_are_rejected(self):
        with self.assertRaisesRegex(storage.InventoryError, "Time format"):
            await self.manager.async_save_settings(
                {"general": {"time_format": "auto", "date_format": "day_first"}}
            )

    async def test_network_fields_labels_and_change_log_are_stored(self):
        device = await self.manager.async_add(
            device_payload(
                "Outdoor camera",
                "wifi",
                network="IoT network",
                vlan="30",
                ssid="House IoT",
                connected_device="Garden AP",
                switch_port="8",
                labels=["IoT", "Security", "Outdoor"],
            )
        )
        self.assertEqual(device["vlan"], "30")
        self.assertEqual(device["labels"], ["IoT", "Outdoor", "Security"])
        updated = await self.manager.async_update(device["id"], {"switch_port": "9"})
        self.assertEqual(updated["switch_port"], "9")
        log = self.manager.data["logs"][-1]
        self.assertEqual(log["action"], "update")
        self.assertEqual(log["changes"], [{"field": "switch_port", "old": "8", "new": "9"}])

    async def test_bulk_import_creates_restorable_backup(self):
        original = await self.manager.async_add(device_payload("Original", "wifi"))
        result = await self.manager.async_import(
            [
                device_payload("Sensor one", "zigbee", mac="00:11:22:33:44:66"),
                device_payload("Sensor two", "zigbee", mac="00:11:22:33:44:77"),
            ]
        )
        self.assertTrue(result["backup_id"])
        self.assertEqual(len(self.manager.data["devices"]), 3)
        await self.manager.async_restore_backup(result["backup_id"])
        self.assertEqual([item["id"] for item in self.manager.data["devices"]], [original["id"]])

    async def test_json_export_and_restore(self):
        await self.manager.async_add(device_payload("Router", "wifi", labels=["Critical"]))
        exported = await self.manager.async_export()
        await self.manager.async_add(
            device_payload("Motion", "zigbee", mac="00:11:22:33:44:88")
        )
        await self.manager.async_restore(exported)
        self.assertEqual(len(self.manager.data["devices"]), 1)
        self.assertEqual(self.manager.data["devices"][0]["labels"], ["Critical"])

    async def test_custom_fields_links_and_admin_url_are_stored(self):
        settings = await self.manager.async_save_settings(
            {
                "custom_fields": [
                    {"label": "Purchase date", "type": "date"},
                    {"label": "PoE", "type": "boolean"},
                ]
            }
        )
        purchase_id, poe_id = [item["id"] for item in settings["custom_fields"]]
        device = await self.manager.async_add(
            device_payload(
                "Managed switch",
                "ethernet",
                admin_url="https://192.168.1.2",
                links=[{"label": "Manual", "url": "https://example.com/manual.pdf"}],
                custom_values={purchase_id: "2026-09-22", poe_id: True},
            )
        )
        self.assertEqual(device["admin_url"], "https://192.168.1.2")
        self.assertEqual(device["links"][0]["label"], "Manual")
        self.assertEqual(device["custom_values"][purchase_id], "2026-09-22")
        self.assertTrue(device["custom_values"][poe_id])

    async def test_invalid_device_url_is_rejected(self):
        with self.assertRaisesRegex(storage.InventoryError, "Admin URL"):
            await self.manager.async_add(
                device_payload("Unsafe", "wifi", admin_url="javascript:alert(1)")
            )

    async def test_attachment_metadata_and_full_zip_round_trip(self):
        device = await self.manager.async_add(device_payload("Router", "wifi"))
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary) / "attachments"
            self.manager.attachments_dir = root
            attachment_id = "attachment123"
            stored_name = files.stored_attachment_name(attachment_id, "manual.pdf")
            target_dir = root / device["id"]
            target_dir.mkdir(parents=True)
            (target_dir / stored_name).write_bytes(b"pdf-content")
            await self.manager.async_add_attachment(
                device["id"],
                {
                    "id": attachment_id,
                    "name": "manual.pdf",
                    "stored_name": stored_name,
                    "content_type": "application/pdf",
                    "size": 11,
                },
            )
            payload = await self.manager.async_export()
            archive = files.build_full_backup(payload, root)
            restored_payload, restored_files = files.parse_full_backup(archive)
            self.assertEqual(restored_payload["data"]["devices"][0]["attachments"][0]["name"], "manual.pdf")
            self.assertEqual(restored_files[f"{device['id']}/{stored_name}"], b"pdf-content")
            updated = await self.manager.async_update(
                device["id"], {"attachments": [], "comments": "Still attached"}
            )
            self.assertEqual(updated["attachments"][0]["id"], attachment_id)
            removed = await self.manager.async_remove_attachment(
                device["id"], attachment_id
            )
            self.assertEqual(removed["name"], "manual.pdf")

    async def test_full_zip_rejects_undeclared_paths(self):
        output = BytesIO()
        with ZipFile(output, "w") as archive:
            archive.writestr("inventory.json", '{"data":{"devices":[]}}')
            archive.writestr("../outside.txt", "unsafe")
        with self.assertRaisesRegex(storage.InventoryError, "invalid path"):
            files.parse_full_backup(output.getvalue())

    async def test_full_zip_rejects_attachment_size_mismatch(self):
        device = await self.manager.async_add(device_payload("Router", "wifi"))
        attachment = {
            "id": "attachment123",
            "name": "manual.pdf",
            "stored_name": "attachment123.pdf",
            "content_type": "application/pdf",
            "size": 99,
        }
        self.manager.data["devices"][0]["attachments"] = [attachment]
        payload = await self.manager.async_export()
        output = BytesIO()
        with ZipFile(output, "w") as archive:
            archive.writestr("inventory.json", json.dumps(payload))
            archive.writestr(
                f"attachments/{device['id']}/attachment123.pdf", b"short"
            )
        with self.assertRaisesRegex(storage.InventoryError, "size mismatch"):
            files.parse_full_backup(output.getvalue())

    async def test_bulk_update_creates_backup_and_updates_selected_fields(self):
        first = await self.manager.async_add(
            device_payload("First", "wifi", labels=["IoT"])
        )
        second = await self.manager.async_add(
            device_payload("Second", "wifi", mac="00:11:22:33:44:99")
        )
        result = await self.manager.async_bulk_update(
            [first["id"], second["id"]],
            {"network": "IoT", "vlan": "30", "device_type": "Camera"},
            "add",
            ["Critical"],
        )
        self.assertEqual(result["updated"], 2)
        self.assertTrue(result["backup_id"])
        for device in self.manager.data["devices"]:
            self.assertEqual(device["network"], "IoT")
            self.assertEqual(device["vlan"], "30")
            self.assertEqual(device["device_type"], "Camera")
            self.assertIn("Critical", device["labels"])
        bulk_logs = [
            item for item in self.manager.data["logs"] if item["action"] == "bulk_update"
        ]
        self.assertEqual(len(bulk_logs), 2)

    async def test_bulk_label_remove_and_replace(self):
        device = await self.manager.async_add(
            device_payload("Tagged", "zigbee", labels=["IoT", "Battery"])
        )
        await self.manager.async_bulk_update([device["id"]], {}, "remove", ["IoT"])
        self.assertEqual(self.manager.data["devices"][0]["labels"], ["Battery"])
        await self.manager.async_bulk_update(
            [device["id"]], {}, "replace", ["Outdoor", "Security"]
        )
        self.assertEqual(
            self.manager.data["devices"][0]["labels"], ["Outdoor", "Security"]
        )

    async def test_home_assistant_labels_replace_matched_device_labels(self):
        device = await self.manager.async_add(
            device_payload("Matched sensor", "zigbee", labels=["IoT"])
        )
        changed = await self.manager.async_sync_ha_labels(
            ["Battery", "Critical"], {device["id"]: ["Battery"]}
        )
        self.assertTrue(changed)
        self.assertEqual(self.manager.data["labels"], ["Battery", "Critical"])
        self.assertEqual(self.manager.data["devices"][0]["labels"], ["Battery"])
        self.assertTrue(self.manager.data["ha_labels_migrated"])
        self.assertEqual(self.manager.data["logs"][-1]["source"], "home_assistant")

    async def test_legacy_tags_are_migrated_to_labels(self):
        device = await self.manager.async_add(
            device_payload("Legacy sensor", "zigbee", labels=["Battery"])
        )
        legacy = dict(self.manager.data)
        legacy["tags"] = legacy.pop("labels")
        legacy_labels = list(legacy["tags"])
        legacy["devices"] = [dict(device)]
        legacy["devices"][0]["tags"] = legacy["devices"][0].pop("labels")

        migrated = storage.InventoryStore(None)

        async def load_legacy():
            return legacy

        migrated._store.async_load = load_legacy
        await migrated.async_load()
        self.assertNotIn("tags", migrated.data)
        self.assertEqual(migrated.data["labels"], legacy_labels)
        self.assertNotIn("tags", migrated.data["devices"][0])
        self.assertEqual(migrated.data["devices"][0]["labels"], ["Battery"])

    async def test_change_log_keeps_latest_500_entries(self):
        for index in range(510):
            self.manager._record_log("settings", details=f"Change {index}")
        self.assertEqual(len(self.manager.data["logs"]), 500)
        self.assertEqual(self.manager.data["logs"][0]["details"], "Change 10")
        self.assertEqual(self.manager.data["logs"][-1]["details"], "Change 509")

    async def test_update_can_be_undone_from_log(self):
        device = await self.manager.async_add(device_payload("Camera", "wifi"))
        await self.manager.async_update(device["id"], {"name": "Front camera"})
        update_log = self.manager.data["logs"][-1]

        reverted = await self.manager.async_undo_log(update_log["id"])

        self.assertEqual(reverted["name"], "Camera")
        self.assertTrue(update_log["undone_by"])
        self.assertEqual(self.manager.data["logs"][-1]["action"], "undo")
        self.assertEqual(
            self.manager.data["logs"][-1]["reverts_log_id"], update_log["id"]
        )
        with self.assertRaisesRegex(storage.InventoryError, "already been undone"):
            await self.manager.async_undo_log(update_log["id"])

    async def test_stale_log_cannot_overwrite_a_newer_change(self):
        device = await self.manager.async_add(device_payload("Camera", "wifi"))
        await self.manager.async_update(device["id"], {"name": "Front camera"})
        older_log = self.manager.data["logs"][-1]
        await self.manager.async_update(device["id"], {"name": "Garage camera"})

        with self.assertRaisesRegex(storage.InventoryError, "changed after"):
            await self.manager.async_undo_log(older_log["id"])

    async def test_battery_replacement_log_is_reversible(self):
        device = await self.manager.async_add(device_payload("Remote", "zigbee"))
        await self.manager.async_record_battery_replacement(
            device["id"], "2026-09-22", "CR2032"
        )
        replacement_log = self.manager.data["logs"][-1]
        self.assertTrue(replacement_log["changes"])

        reverted = await self.manager.async_undo_log(replacement_log["id"])

        self.assertEqual(reverted["battery_last_replaced_at"], "")
        self.assertEqual(reverted["battery_history"], [])

    async def test_required_fields_and_ip_validation(self):
        with self.assertRaisesRegex(storage.InventoryError, "Type"):
            await self.manager.async_add(
                device_payload("Incomplete", "zigbee", device_type="")
            )
        with self.assertRaisesRegex(storage.InventoryError, "IP address"):
            await self.manager.async_add(
                device_payload("No IP", "wifi", ip_address="")
            )

    async def test_child_device_does_not_require_mac_or_ip(self):
        device = await self.manager.async_add(
            device_payload(
                "Child channel",
                "wifi",
                mac="",
                ip_address="",
                ha_device_kind="child",
                parent_ha_device_id="parent-1",
                parent_device_name="Parent hub",
                ha_config_entry_id="entry-1",
                ha_config_subentry_id="subentry-1",
            )
        )
        self.assertEqual(device["ha_device_kind"], "child")
        self.assertEqual(device["parent_ha_device_id"], "parent-1")
        self.assertEqual(device["mac"], "")

    async def test_battery_entity_and_replacement_history(self):
        device = await self.manager.async_add(
            device_payload(
                "Door sensor",
                "zigbee",
                battery_entity_id="sensor.door_battery",
                battery_last_replaced_at="2026-01-10",
            )
        )
        self.assertEqual(device["battery_entity_id"], "sensor.door_battery")
        self.assertEqual(len(device["battery_history"]), 1)

        updated = await self.manager.async_update(
            device["id"], {"battery_last_replaced_at": "2026-05-20"}
        )
        self.assertEqual(len(updated["battery_history"]), 2)
        self.assertEqual(updated["battery_history"][-1]["replaced_at"], "2026-05-20")

        replaced = await self.manager.async_record_battery_replacement(
            device["id"], "2026-09-22", "CR2032"
        )
        self.assertEqual(replaced["battery_last_replaced_at"], "2026-09-22")
        self.assertEqual(replaced["battery_history"][-1]["note"], "CR2032")
        self.assertEqual(self.manager.data["logs"][-1]["action"], "battery_replaced")

    async def test_invalid_battery_replacement_date_is_rejected(self):
        device = await self.manager.async_add(device_payload("Remote", "zigbee"))
        with self.assertRaisesRegex(storage.InventoryError, "YYYY-MM-DD"):
            await self.manager.async_record_battery_replacement(
                device["id"], "22/09/2026"
            )

    async def test_primary_entity_is_stored_as_complete_entity_id(self):
        device = await self.manager.async_add(
            device_payload(
                "Window sensor",
                "zigbee",
                primary_entity_id="binary_sensor.window_contact",
            )
        )
        self.assertEqual(
            device["primary_entity_id"], "binary_sensor.window_contact"
        )
        with self.assertRaisesRegex(storage.InventoryError, "complete entity ID"):
            await self.manager.async_update(
                device["id"], {"primary_entity_id": "window_contact"}
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

    def test_device_registry_code_uses_current_iterables(self):
        source = (
            Path(__file__).parents[1]
            / "custom_components"
            / "network_inventory"
            / "websocket.py"
        ).read_text(encoding="utf-8")
        self.assertNotIn("registry.devices.values()", source)
        self.assertIn("device_registry.child_devices", source)
        self.assertIn("device.config_entry_id", source)
        self.assertIn("def _battery_entities", source)
        self.assertIn("websocket_battery_replaced", source)
        self.assertIn("websocket_undo_log", source)
        self.assertIn("def _home_assistant_entities", source)
        self.assertIn("def _primary_entity_id", source)
        self.assertIn("label_registry as lr", source)
        self.assertIn("async_sync_labels_from_home_assistant", source)
        self.assertIn("async_update_device(entry.id, labels=label_ids)", source)
        frontend_source = (
            Path(__file__).parents[1]
            / "custom_components"
            / "network_inventory"
            / "frontend"
            / "network-inventory-panel.js"
        ).read_text(encoding="utf-8")
        self.assertIn("availableUpdate()", frontend_source)
        self.assertIn('href="/config/updates"', frontend_source)
        self.assertIn(
            'this.nav("devices", "mdi:devices", "devices", this.data.devices.length)',
            frontend_source,
        )


if __name__ == "__main__":
    unittest.main()
