"""Authenticated HTTP API for attachments and full backups."""

from __future__ import annotations

import asyncio
import json
import mimetypes
from pathlib import Path
from typing import Any
from urllib.parse import quote
from uuid import uuid4

from aiohttp import web
from homeassistant.components.http import KEY_HASS, HomeAssistantView
from homeassistant.core import HomeAssistant

from .const import DOMAIN, MAX_ATTACHMENT_SIZE, MAX_BACKUP_SIZE
from .files import (
    backup_filename,
    build_full_backup,
    finish_attachment_restore,
    parse_full_backup,
    rollback_attachment_restore,
    stage_attachment_restore,
    stored_attachment_name,
)
from .storage import InventoryError, InventoryStore


def async_register_views(hass: HomeAssistant) -> None:
    """Register authenticated file and backup views."""
    hass.http.register_view(NetworkInventoryAttachmentCollectionView)
    hass.http.register_view(NetworkInventoryAttachmentView)
    hass.http.register_view(NetworkInventoryNoteAttachmentsView)
    hass.http.register_view(NetworkInventoryNoteAttachmentView)
    hass.http.register_view(NetworkInventoryFullBackupView)
    hass.http.register_view(NetworkInventoryFullRestoreView)


def _manager(request: web.Request) -> InventoryStore:
    return request.app[KEY_HASS].data[DOMAIN]["manager"]


def _require_admin(request: web.Request) -> None:
    user = request.get("hass_user")
    if user is None or not user.is_admin:
        raise web.HTTPForbidden()


async def _uploaded_file(request: web.Request, limit: int) -> tuple[str, str, bytes]:
    """Read one multipart file with a strict size limit."""
    request._client_max_size = limit + (1024 * 1024)  # noqa: SLF001
    reader = await request.multipart()
    field = await reader.next()
    if field is None or field.name != "file" or not field.filename:
        raise InventoryError("A file is required")
    content = bytearray()
    while chunk := await field.read_chunk():
        content.extend(chunk)
        if len(content) > limit:
            raise InventoryError("The uploaded file is too large")
    return (
        Path(field.filename.replace("\\", "/")).name[:255],
        str(mimetypes.guess_type(field.filename)[0] or "application/octet-stream"),
        bytes(content),
    )


class NetworkInventoryAttachmentCollectionView(HomeAssistantView):
    """Upload an attachment for one inventory device."""

    url = "/api/network_inventory/devices/{device_id}/attachments"
    name = "api:network_inventory:attachments"
    requires_auth = True

    async def post(self, request: web.Request, device_id: str) -> web.Response:
        _require_admin(request)
        manager = _manager(request)
        try:
            await manager.async_get_device(device_id)
            name, content_type, content = await _uploaded_file(
                request, MAX_ATTACHMENT_SIZE
            )
            attachment_id = uuid4().hex
            stored_name = stored_attachment_name(attachment_id, name)
            target_dir = manager.attachments_dir / device_id
            target = target_dir / stored_name
            await asyncio.to_thread(target_dir.mkdir, parents=True, exist_ok=True)
            await asyncio.to_thread(target.write_bytes, content)
            try:
                attachment = await manager.async_add_attachment(
                    device_id,
                    {
                        "id": attachment_id,
                        "name": name,
                        "stored_name": stored_name,
                        "content_type": content_type,
                        "size": len(content),
                    },
                )
            except Exception:
                await asyncio.to_thread(target.unlink, missing_ok=True)
                raise
        except InventoryError as err:
            return web.json_response({"error": str(err)}, status=400)
        return web.json_response(attachment)


class NetworkInventoryAttachmentView(HomeAssistantView):
    """Download or delete one device attachment."""

    url = "/api/network_inventory/devices/{device_id}/attachments/{attachment_id}"
    name = "api:network_inventory:attachment"
    requires_auth = True

    async def get(
        self, request: web.Request, device_id: str, attachment_id: str
    ) -> web.StreamResponse:
        _require_admin(request)
        try:
            device = await _manager(request).async_get_device(device_id)
            attachment = _find_attachment(device, attachment_id)
        except InventoryError as err:
            raise web.HTTPNotFound(text=str(err)) from err
        target = _manager(request).attachments_dir / device_id / attachment["stored_name"]
        if not target.is_file():
            raise web.HTTPNotFound(text="Attachment file not found")
        response = web.FileResponse(target)
        response.content_type = attachment["content_type"]
        response.headers["Content-Disposition"] = (
            f"attachment; filename*=UTF-8''{quote(attachment['name'])}"
        )
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

    async def delete(
        self, request: web.Request, device_id: str, attachment_id: str
    ) -> web.Response:
        _require_admin(request)
        try:
            attachment = await _manager(request).async_remove_attachment(
                device_id, attachment_id
            )
        except InventoryError as err:
            return web.json_response({"error": str(err)}, status=404)
        target = _manager(request).attachments_dir / device_id / attachment["stored_name"]
        await asyncio.to_thread(target.unlink, missing_ok=True)
        return web.json_response({"deleted": True})


class NetworkInventoryNoteAttachmentsView(HomeAssistantView):
    """Upload an attachment to a note."""

    url = "/api/network_inventory/notes/{note_id}/attachments"
    name = "api:network_inventory:note_attachments"
    requires_auth = True

    async def post(self, request: web.Request, note_id: str) -> web.Response:
        _require_admin(request)
        manager = _manager(request)
        try:
            await manager.async_get_note(note_id)
            name, content_type, content = await _uploaded_file(request, MAX_ATTACHMENT_SIZE)
            attachment_id = uuid4().hex
            stored_name = stored_attachment_name(attachment_id, name)
            target_dir = manager.attachments_dir / f"note-{note_id}"
            target = target_dir / stored_name
            await asyncio.to_thread(target_dir.mkdir, parents=True, exist_ok=True)
            await asyncio.to_thread(target.write_bytes, content)
            try:
                attachment = await manager.async_add_note_attachment(note_id, {
                    "id": attachment_id, "name": name, "stored_name": stored_name,
                    "content_type": content_type, "size": len(content),
                })
            except Exception:
                await asyncio.to_thread(target.unlink, missing_ok=True)
                raise
        except InventoryError as err:
            return web.json_response({"error": str(err)}, status=400)
        return web.json_response(attachment)


class NetworkInventoryNoteAttachmentView(HomeAssistantView):
    """Download or delete a note attachment."""

    url = "/api/network_inventory/notes/{note_id}/attachments/{attachment_id}"
    name = "api:network_inventory:note_attachment"
    requires_auth = True

    async def get(self, request: web.Request, note_id: str, attachment_id: str) -> web.StreamResponse:
        _require_admin(request)
        try:
            note = await _manager(request).async_get_note(note_id)
            attachment = _find_attachment(note, attachment_id)
        except InventoryError as err:
            raise web.HTTPNotFound(text=str(err)) from err
        target = _manager(request).attachments_dir / f"note-{note_id}" / attachment["stored_name"]
        if not target.is_file():
            raise web.HTTPNotFound(text="Attachment file not found")
        response = web.FileResponse(target)
        response.content_type = attachment["content_type"]
        response.headers["Content-Disposition"] = f"attachment; filename*=UTF-8''{quote(attachment['name'])}"
        response.headers["X-Content-Type-Options"] = "nosniff"
        return response

    async def delete(self, request: web.Request, note_id: str, attachment_id: str) -> web.Response:
        _require_admin(request)
        try:
            attachment = await _manager(request).async_remove_note_attachment(note_id, attachment_id)
        except InventoryError as err:
            return web.json_response({"error": str(err)}, status=404)
        target = _manager(request).attachments_dir / f"note-{note_id}" / attachment["stored_name"]
        await asyncio.to_thread(target.unlink, missing_ok=True)
        return web.json_response({"deleted": True})


class NetworkInventoryFullBackupView(HomeAssistantView):
    """Download inventory data and attachments as one ZIP."""

    url = "/api/network_inventory/backup"
    name = "api:network_inventory:backup"
    requires_auth = True

    async def get(self, request: web.Request) -> web.Response:
        _require_admin(request)
        manager = _manager(request)
        payload = await manager.async_export()
        try:
            content = await asyncio.to_thread(
                build_full_backup, payload, manager.attachments_dir
            )
        except InventoryError as err:
            return web.json_response({"error": str(err)}, status=400)
        return web.Response(
            body=content,
            content_type="application/zip",
            headers={"Content-Disposition": f'attachment; filename="{backup_filename()}"'},
        )


class NetworkInventoryFullRestoreView(HomeAssistantView):
    """Restore a full ZIP backup, including attachments."""

    url = "/api/network_inventory/restore"
    name = "api:network_inventory:restore"
    requires_auth = True

    async def post(self, request: web.Request) -> web.Response:
        _require_admin(request)
        manager = _manager(request)
        hass: HomeAssistant = request.app[KEY_HASS]
        previous: Path | None = None
        try:
            name, _content_type, content = await _uploaded_file(
                request, MAX_BACKUP_SIZE
            )
            if name.lower().endswith(".json"):
                payload = json.loads(content.decode("utf-8"))
                result = await manager.async_restore(payload)
            else:
                payload, files = await asyncio.to_thread(parse_full_backup, content)
                _target, previous = await asyncio.to_thread(
                    stage_attachment_restore, manager.attachments_dir, files
                )
                try:
                    result = await manager.async_restore(payload)
                except Exception:
                    await asyncio.to_thread(
                        rollback_attachment_restore,
                        manager.attachments_dir,
                        previous,
                    )
                    raise
                await asyncio.to_thread(finish_attachment_restore, previous)
            # Import locally to avoid an import cycle while the integration starts.
            from .websocket import _push_device_labels_to_home_assistant

            for device in result["devices"]:
                _push_device_labels_to_home_assistant(hass, device)
        except (InventoryError, UnicodeDecodeError, json.JSONDecodeError) as err:
            return web.json_response({"error": str(err)}, status=400)
        return web.json_response({"restored": True})


def _find_attachment(device: dict[str, Any], attachment_id: str) -> dict[str, Any]:
    attachment = next(
        (
            item
            for item in device.get("attachments", [])
            if item.get("id") == attachment_id
        ),
        None,
    )
    if attachment is None:
        raise InventoryError("Attachment not found")
    return attachment
