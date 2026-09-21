"""Official UniFi Cloud API client for Network Inventory."""

from __future__ import annotations

import asyncio
from copy import deepcopy
from datetime import UTC, datetime
import re
from typing import Any
from urllib.parse import quote

from aiohttp import ClientError, ClientResponseError, ClientTimeout

from homeassistant.core import HomeAssistant
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.storage import Store

from .const import UNIFI_STORAGE_KEY

SITE_MANAGER_URL = "https://api.ui.com/v1/sites"
CONNECTOR_URL = "https://api.ui.com/v1/connector/consoles/{host}/proxy/network/integration"


class UniFiError(ValueError):
    """Raised when UniFi Cloud cannot complete a request."""


def normalize_mac(value: Any) -> str:
    """Return a comparable lowercase hardware address."""
    cleaned = re.sub(r"[^0-9a-f]", "", str(value or "").lower())
    return cleaned if len(cleaned) >= 12 else ""


def match_unifi_items(
    inventory: list[dict[str, Any]], items: list[dict[str, Any]]
) -> tuple[dict[str, dict[str, Any]], list[dict[str, Any]]]:
    """Match inventory and UniFi items by MAC without mutating either list."""
    by_mac = {
        normalize_mac(item.get("mac")): item
        for item in items
        if normalize_mac(item.get("mac"))
    }
    inventory_by_mac = {
        normalize_mac(device.get("mac")): device
        for device in inventory
        if normalize_mac(device.get("mac"))
    }
    matches: dict[str, dict[str, Any]] = {}
    for device in inventory:
        item = by_mac.get(normalize_mac(device.get("mac")))
        if item:
            matches[str(device["id"])] = deepcopy(item)
    enriched = []
    for item in items:
        copy = deepcopy(item)
        device = inventory_by_mac.get(normalize_mac(item.get("mac")))
        copy["inventory_id"] = device.get("id") if device else ""
        enriched.append(copy)
    return matches, enriched


class UniFiCloudManager:
    """Store UniFi credentials privately and retrieve current network data."""

    def __init__(self, hass: HomeAssistant) -> None:
        self._hass = hass
        self._store: Store[dict[str, Any]] = Store(
            hass, 1, UNIFI_STORAGE_KEY, private=True, atomic_writes=True
        )
        self._lock = asyncio.Lock()
        self.data: dict[str, Any] = {}
        self.items: list[dict[str, Any]] = []
        self.last_error = ""

    async def async_load(self) -> None:
        """Load credentials without contacting the cloud during HA startup."""
        self.data = await self._store.async_load() or {}
        self.data.setdefault("api_key", "")
        self.data.setdefault("host_id", "")
        self.data.setdefault("site_id", "")
        self.data.setdefault("site_name", "")
        self.data.setdefault("available_sites", [])
        self.data.setdefault("last_refreshed", "")

    def status(self) -> dict[str, Any]:
        """Return safe configuration state; never expose the API key."""
        return {
            "configured": bool(self.data.get("api_key")),
            "connected": bool(
                self.data.get("api_key")
                and self.data.get("host_id")
                and self.data.get("site_id")
            ),
            "site_id": self.data.get("site_id", ""),
            "site_name": self.data.get("site_name", ""),
            "available_sites": deepcopy(self.data.get("available_sites", [])),
            "last_refreshed": self.data.get("last_refreshed", ""),
            "last_error": self.last_error,
            "item_count": len(self.items),
        }

    async def async_connect(
        self, api_key: str | None = None, host_id: str = "", site_id: str = ""
    ) -> dict[str, Any]:
        """Validate a key and activate a selected console/site."""
        async with self._lock:
            key = str(api_key or self.data.get("api_key") or "").strip()
            if not key:
                raise UniFiError("UniFi API key is required")
            sites = await self._site_manager_sites(key)
            if not sites:
                raise UniFiError("No UniFi Network sites are available for this API key")

            choices = [self._site_choice(item) for item in sites]
            selected = next(
                (
                    item
                    for item in choices
                    if item["host_id"] == host_id and item["site_id"] == site_id
                ),
                None,
            )
            if selected is None and len(choices) == 1:
                selected = choices[0]

            self.data["api_key"] = key
            self.data["available_sites"] = choices
            if selected:
                self.data.update(
                    {
                        "host_id": selected["host_id"],
                        "site_id": selected["site_id"],
                        "site_name": selected["name"],
                    }
                )
            else:
                self.data.update({"host_id": "", "site_id": "", "site_name": ""})
            await self._store.async_save(self.data)

        if selected:
            await self.async_refresh()
        return self.status()

    async def async_disconnect(self) -> None:
        """Remove credentials and cached UniFi data."""
        async with self._lock:
            self.data = {
                "api_key": "",
                "host_id": "",
                "site_id": "",
                "site_name": "",
                "available_sites": [],
                "last_refreshed": "",
            }
            self.items = []
            self.last_error = ""
            await self._store.async_save(self.data)

    async def async_ensure_loaded(self) -> None:
        """Populate the in-memory cache once after a restart."""
        if self.status()["connected"] and not self.items and not self.last_error:
            try:
                await self.async_refresh()
            except UniFiError as err:
                self.last_error = str(err)

    async def async_refresh(self) -> list[dict[str, Any]]:
        """Fetch connected clients and adopted UniFi infrastructure."""
        key = self.data.get("api_key", "")
        host = self.data.get("host_id", "")
        site = self.data.get("site_id", "")
        if not key or not host or not site:
            raise UniFiError("Select a UniFi console and site first")

        base = CONNECTOR_URL.format(host=quote(host, safe=""))
        try:
            clients, devices = await asyncio.gather(
                self._network_page(base, key, f"/v1/sites/{quote(site, safe='')}/clients"),
                self._network_page(base, key, f"/v1/sites/{quote(site, safe='')}/devices"),
            )
        except UniFiError as err:
            self.last_error = str(err)
            raise

        uplinks = {str(item.get("id")): item for item in devices}
        items = [self._client_item(item, uplinks) for item in clients]
        items.extend(self._device_item(item) for item in devices)
        items.sort(key=lambda item: (item["kind"] != "client", item["name"].casefold()))
        self.items = items
        self.last_error = ""
        self.data["last_refreshed"] = datetime.now(UTC).isoformat()
        await self._store.async_save(self.data)
        return deepcopy(self.items)

    async def _site_manager_sites(self, key: str) -> list[dict[str, Any]]:
        return await self._paged_request(SITE_MANAGER_URL, key, site_manager=True)

    async def _network_page(self, base: str, key: str, path: str) -> list[dict[str, Any]]:
        return await self._paged_request(base + path, key, site_manager=False)

    async def _paged_request(
        self, url: str, key: str, *, site_manager: bool
    ) -> list[dict[str, Any]]:
        session = async_get_clientsession(self._hass)
        results: list[dict[str, Any]] = []
        token = ""
        offset = 0
        try:
            for _ in range(100):
                params: dict[str, Any]
                if site_manager:
                    params = {"pageSize": "100"}
                    if token:
                        params["nextToken"] = token
                else:
                    params = {"limit": 200, "offset": offset}
                async with session.get(
                    url,
                    headers={"X-API-Key": key, "Accept": "application/json"},
                    params=params,
                    timeout=ClientTimeout(total=35),
                ) as response:
                    response.raise_for_status()
                    payload = await response.json(content_type=None)
                page = payload.get("data", []) if isinstance(payload, dict) else []
                results.extend(item for item in page if isinstance(item, dict))
                if site_manager:
                    token = str(payload.get("nextToken") or "")
                    if not token:
                        break
                else:
                    total = int(payload.get("totalCount", len(results)) or 0)
                    if len(results) >= total or not page:
                        break
                    offset += len(page)
        except ClientResponseError as err:
            if err.status in (401, 403):
                raise UniFiError("The UniFi API key is invalid or lacks permission") from err
            raise UniFiError(f"UniFi Cloud returned HTTP {err.status}") from err
        except (ClientError, TimeoutError, ValueError) as err:
            raise UniFiError(f"Could not contact UniFi Cloud: {err}") from err
        return results

    @staticmethod
    def _site_choice(site: dict[str, Any]) -> dict[str, str]:
        meta = site.get("meta") if isinstance(site.get("meta"), dict) else {}
        return {
            "host_id": str(site.get("hostId") or ""),
            "site_id": str(site.get("siteId") or ""),
            "name": str(meta.get("desc") or meta.get("name") or site.get("siteId") or "Site"),
            "gateway_mac": str(meta.get("gatewayMac") or ""),
        }

    @staticmethod
    def _client_item(
        client: dict[str, Any], uplinks: dict[str, dict[str, Any]]
    ) -> dict[str, Any]:
        connection = str(client.get("type") or "").upper()
        uplink = uplinks.get(str(client.get("uplinkDeviceId") or ""), {})
        return {
            "id": str(client.get("id") or ""),
            "kind": "client",
            "name": str(client.get("name") or client.get("macAddress") or "Unknown client"),
            "mac": str(client.get("macAddress") or ""),
            "ip_address": str(client.get("ipAddress") or ""),
            "protocol": "wifi" if connection == "WIRELESS" else "ethernet",
            "connection_type": connection.title(),
            "connected_at": str(client.get("connectedAt") or ""),
            "uplink_id": str(client.get("uplinkDeviceId") or ""),
            "uplink_name": str(uplink.get("name") or ""),
            "uplink_model": str(uplink.get("model") or ""),
            "uplink_ip": str(uplink.get("ipAddress") or ""),
            "device_type": "Computer",
            "brand": "",
            "model": "",
            "status": "online",
        }

    @staticmethod
    def _device_item(device: dict[str, Any]) -> dict[str, Any]:
        features = set(device.get("features") or [])
        if "accessPoint" in features:
            device_type = "Access Point"
        elif "gateway" in features:
            device_type = "Gateway"
        elif "switching" in features:
            device_type = "Switch"
        else:
            device_type = "Other"
        return {
            "id": str(device.get("id") or ""),
            "kind": "infrastructure",
            "name": str(device.get("name") or device.get("model") or "UniFi device"),
            "mac": str(device.get("macAddress") or ""),
            "ip_address": str(device.get("ipAddress") or ""),
            "protocol": "ethernet",
            "connection_type": "UniFi infrastructure",
            "connected_at": "",
            "uplink_id": "",
            "uplink_name": "",
            "uplink_model": "",
            "uplink_ip": "",
            "device_type": device_type,
            "brand": "Ubiquiti",
            "model": str(device.get("model") or ""),
            "firmware_version": str(device.get("firmwareVersion") or ""),
            "status": "online" if device.get("state") == "ONLINE" else "offline",
        }
