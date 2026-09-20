"""Constants for Network Inventory."""

DOMAIN = "network_inventory"
NAME = "Network Inventory"
STORAGE_KEY = f"{DOMAIN}.data"
STORAGE_VERSION = 1
PANEL_URL = "/network_inventory_static"
IP_PROTOCOLS = {"wifi", "ethernet"}

DEFAULT_PROTOCOLS = {
    "wifi": {"label": "Wi-Fi", "start": 1001, "end": 1999, "color": "#2563eb"},
    "zigbee": {"label": "Zigbee", "start": 2001, "end": 2999, "color": "#0891b2"},
    "bluetooth": {"label": "Bluetooth", "start": 3001, "end": 3999, "color": "#d97706"},
    "thread": {"label": "Thread", "start": 4001, "end": 4999, "color": "#7c3aed"},
    "zwave": {"label": "Z-Wave", "start": 5001, "end": 5999, "color": "#db2777"},
    "ethernet": {"label": "Ethernet", "start": 6001, "end": 6999, "color": "#059669"},
    "matter": {"label": "Matter", "start": 7001, "end": 7999, "color": "#4f46e5"},
    "other": {"label": "Other", "start": 9001, "end": 9999, "color": "#64748b"},
}

DEFAULT_DEVICE_TYPES = [
    "Access Point",
    "Bridge",
    "Camera",
    "Computer",
    "Controller",
    "Light",
    "Media Player",
    "Mobile",
    "Router",
    "Sensor",
    "Server",
    "Switch",
    "Thermostat",
    "Other",
]
