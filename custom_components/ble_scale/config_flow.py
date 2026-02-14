"""Config flow for BLE Scale integration."""
from __future__ import annotations

import asyncio
import logging
from typing import Any

import voluptuous as vol
from homeassistant import config_entries
from homeassistant.components.bluetooth import (
    BluetoothServiceInfo,
    async_discovered_service_info,
)
from homeassistant.const import CONF_ADDRESS, CONF_NAME
from homeassistant.core import HomeAssistant
from homeassistant.data_entry_flow import FlowResult

from .const import CONF_SCALE_MODEL, DOMAIN, SCALE_MODELS

_LOGGER = logging.getLogger(__name__)

STEP_USER_DATA_SCHEMA = vol.Schema(
    {
        vol.Required(CONF_ADDRESS): str,
        vol.Required(CONF_NAME): str,
        vol.Required(CONF_SCALE_MODEL): vol.In(SCALE_MODELS),
    }
)


class BLEScaleConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Handle a config flow for BLE Scale."""

    VERSION = 1

    def __init__(self) -> None:
        """Initialize the config flow."""
        self._discovered_devices: dict[str, BluetoothServiceInfo] = {}

    async def async_step_user(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Handle the initial step."""
        if user_input is not None:
            await self.async_set_unique_id(user_input[CONF_ADDRESS])
            self._abort_if_unique_id_configured()

            return self.async_create_entry(
                title=user_input[CONF_NAME],
                data=user_input,
            )

        return self.async_show_form(
            step_id="user", data_schema=STEP_USER_DATA_SCHEMA
        )

    async def async_step_bluetooth(
        self, discovery_info: BluetoothServiceInfo
    ) -> FlowResult:
        """Handle the Bluetooth discovery step."""
        await self.async_set_unique_id(discovery_info.address)
        self._abort_if_unique_id_configured()

        self._discovered_devices[discovery_info.address] = discovery_info

        return await self.async_step_bluetooth_confirm()

    async def async_step_bluetooth_confirm(
        self, user_input: dict[str, Any] | None = None
    ) -> FlowResult:
        """Confirm discovery of a BLE scale."""
        if user_input is not None:
            device = self._discovered_devices.get(
                user_input.get(CONF_ADDRESS, "")
            )
            if device:
                return self.async_create_entry(
                    title=user_input.get(CONF_NAME, device.name or "BLE Scale"),
                    data={
                        CONF_ADDRESS: device.address,
                        CONF_NAME: user_input.get(CONF_NAME, device.name or "BLE Scale"),
                        CONF_SCALE_MODEL: user_input.get(CONF_SCALE_MODEL, "auto"),
                    },
                )

        schema = vol.Schema(
            {
                vol.Required(
                    CONF_ADDRESS,
                    default=list(self._discovered_devices.keys())[0]
                    if self._discovered_devices
                    else None,
                ): vol.In(self._discovered_devices),
                vol.Required(CONF_NAME): str,
                vol.Required(CONF_SCALE_MODEL): vol.In(SCALE_MODELS),
            }
        )

        return self.async_show_form(
            step_id="bluetooth_confirm",
            data_schema=schema,
            description_placeholders={
                "devices": ", ".join(
                    [
                        f"{info.name} ({info.address})"
                        for info in self._discovered_devices.values()
                    ]
                ),
            },
        )

    @staticmethod
    def async_get_discovery_flow_handlers() -> dict[str, type]:
        """Return the discovery flow handlers for BLE Scale."""
        return {
            "bluetooth": BLEScaleConfigFlow,
        }
