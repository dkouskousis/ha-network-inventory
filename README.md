# Network Inventory for Home Assistant

A small, local device inventory for Home Assistant. It adds a dedicated sidebar panel for smart-home and network devices, including equipment that is not represented by an entity in Home Assistant.

## Features

- Permanent numeric Device ID for every device
- Separate configurable number range for each protocol
- Manual device management
- Import from the Home Assistant Device Registry
- Official UniFi Cloud integration for connected clients and adopted network devices
- One-click review before adding a UniFi client to the inventory
- UniFi badges and live uplink/AP details for matching stored devices
- Inventory/UniFi IP mismatch warnings with confirmed one-click Inventory updates
- Duplicate IP detection and filtering, including the conflicting device names
- Open matching devices in the UniFi portal and display the last UniFi refresh time
- Optional NIIMBOT integration with per-device D11H label printing
- Configurable D11H label dimensions and safe print margins
- Review imported devices in a pre-filled form before saving
- Configurable brand list with automatic additions during import
- Import and export compatible CSV files
- Search and protocol filters
- Detailed filters for protocol, type, brand, area, and status
- Home Assistant area suggestions with support for custom areas
- Optional Device ID reassignment after a protocol change
- Responsive desktop and mobile interface
- English and Greek UI
- Data included in Home Assistant backups
- Admin-only access through Home Assistant authentication

## Default Device ID ranges

| Protocol | Range |
| --- | ---: |
| Wi-Fi | 1001–1999 |
| Zigbee | 2001–2999 |
| Bluetooth | 3001–3999 |
| Thread | 4001–4999 |
| Z-Wave | 5001–5999 |
| Ethernet | 6001–6999 |
| Matter | 7001–7999 |
| Other | 9001–9999 |

The next number is issued atomically when a device is created. Device IDs do not change when a device is edited or moved to another protocol. Deleted IDs are never reused. Ranges can be edited from the Settings tab, provided they remain non-overlapping and still contain existing IDs.

## Installation with HACS

1. Open HACS.
2. Open **Integrations**.
3. Select the three-dot menu and **Custom repositories**.
4. Add `https://github.com/dkouskousis/ha-network-inventory` as an **Integration**.
5. Download **Network Inventory**.
6. Restart Home Assistant.
7. Open **Settings → Devices & services → Add integration**.
8. Search for **Network Inventory** and add it.

The **Network Inventory** entry will then appear in the Home Assistant sidebar for administrator accounts.

## Manual installation

Copy `custom_components/network_inventory` to the `custom_components` directory in the Home Assistant configuration folder. Restart Home Assistant and add the integration from **Settings → Devices & services**.

## CSV columns

The importer recognises these spreadsheet columns:

```text
Device Code, MAC / IEEE Address, Device IP, Device Type, Brand,
Area, Device Name, Device ID, Entity Name, Comments, Protocol
```

`Device Name`, `Device Type`, `Brand`, `Area`, `MAC / IEEE Address`, and `Protocol` are required. `Device IP` is also required for Wi-Fi and Ethernet devices. `Device Code` can be omitted to assign the next available permanent ID automatically. The importer also accepts `Wi-Fi`, `ZigBee`, `Bluetooth`, `Thread`, `Z-Wave`, `Ethernet`, `Matter`, and `Other` protocol values.

## Storage and privacy

Inventory data is stored locally in Home Assistant's private `.storage` directory. The panel and its WebSocket commands require an administrator account. The UniFi API key is kept in a separate private Home Assistant Store and is never returned to the browser after submission.

## UniFi Cloud

Open **Network Inventory → Integrations**, create a read-only API key at [UniFi Site Manager](https://unifi.ui.com/settings/api-keys), and paste it into the UniFi Cloud card. If the account contains more than one site, select the Dream Machine site to activate. The UniFi tab then lists connected clients and adopted UniFi infrastructure. Matching with inventory devices uses the MAC address.

The official UniFi Network API returns currently connected clients. Offline UniFi infrastructure remains visible through the adopted-devices endpoint, while disconnected client devices are not included until they reconnect.
