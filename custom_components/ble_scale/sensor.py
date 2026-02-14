"""Sensor platform for BLE Scale integration."""
from __future__ import annotations

import asyncio
import logging
from dataclasses import dataclass
from typing import Any

from bleak import BleakClient, BleakScanner
from homeassistant.components.sensor import (
    SensorEntity,
    SensorEntityDescription,
    SensorStateClass,
)
from homeassistant.const import CONF_ADDRESS, CONF_NAME, UnitOfMass, UnitOfTemperature
from homeassistant.core import HomeAssistant, callback
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.update_coordinator import (
    CoordinatorEntity,
    DataUpdateCoordinator,
    UpdateFailed,
)

from . import ConfigEntry
from .const import CONF_SCALE_MODEL, METRIC_ICONS, METRIC_UNITS

_LOGGER = logging.getLogger(__name__)

SCAN_INTERVAL = 300  # 5 minutes


@dataclass
class BLEScaleSensorEntityDescription(SensorEntityDescription):
    """Describes a BLE Scale sensor entity."""

    metric_key: str | None = None


SENSOR_DESCRIPTIONS = [
    BLEScaleSensorEntityDescription(
        key="weight",
        name="Weight",
        metric_key="weight",
        native_unit_of_measurement=UnitOfMass.KILOGRAMS,
        state_class=SensorStateClass.MEASUREMENT,
        icon=METRIC_ICONS.get("weight"),
    ),
    BLEScaleSensorEntityDescription(
        key="fat_percentage",
        name="Fat Percentage",
        metric_key="fat_percentage",
        native_unit_of_measurement="%",
        state_class=SensorStateClass.MEASUREMENT,
        icon=METRIC_ICONS.get("fat_percentage"),
    ),
    BLEScaleSensorEntityDescription(
        key="muscle_mass",
        name="Muscle Mass",
        metric_key="muscle_mass",
        native_unit_of_measurement=UnitOfMass.KILOGRAMS,
        state_class=SensorStateClass.MEASUREMENT,
        icon=METRIC_ICONS.get("muscle_mass"),
    ),
    BLEScaleSensorEntityDescription(
        key="water_percentage",
        name="Water Percentage",
        metric_key="water_percentage",
        native_unit_of_measurement="%",
        state_class=SensorStateClass.MEASUREMENT,
        icon=METRIC_ICONS.get("water_percentage"),
    ),
    BLEScaleSensorEntityDescription(
        key="bone_mass",
        name="Bone Mass",
        metric_key="bone_mass",
        native_unit_of_measurement=UnitOfMass.KILOGRAMS,
        state_class=SensorStateClass.MEASUREMENT,
        icon=METRIC_ICONS.get("bone_mass"),
    ),
    BLEScaleSensorEntityDescription(
        key="basal_metabolism",
        name="Basal Metabolism",
        metric_key="basal_metabolism",
        native_unit_of_measurement="kcal",
        state_class=SensorStateClass.MEASUREMENT,
        icon=METRIC_ICONS.get("basal_metabolism"),
    ),
    BLEScaleSensorEntityDescription(
        key="bmi",
        name="BMI",
        metric_key="bmi",
        state_class=SensorStateClass.MEASUREMENT,
        icon=METRIC_ICONS.get("bmi"),
    ),
]


async def async_setup_entry(
    hass: HomeAssistant,
    entry: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
) -> None:
    """Set up BLE Scale sensors from a config entry."""
    address = entry.data[CONF_ADDRESS]
    name = entry.data[CONF_NAME]
    scale_model = entry.data.get(CONF_SCALE_MODEL, "auto")

    coordinator = BLEScaleDataUpdateCoordinator(
        hass, address, name, scale_model
    )
    await coordinator.async_config_entry_first_refresh()

    async_add_entities(
        BLEScaleSensorEntity(coordinator, entry, description)
        for description in SENSOR_DESCRIPTIONS
    )


class BLEScaleDataUpdateCoordinator(DataUpdateCoordinator):
    """Data update coordinator for BLE Scale."""

    def __init__(
        self,
        hass: HomeAssistant,
        address: str,
        name: str,
        scale_model: str,
    ) -> None:
        """Initialize the coordinator."""
        super().__init__(
            hass,
            _LOGGER,
            name=f"BLE Scale {name}",
            update_interval=300,  # 5 minutes
        )
        self.address = address
        self.name = name
        self.scale_model = scale_model

    async def _async_update_data(self) -> dict[str, Any]:
        """Fetch data from the BLE scale."""
        try:
            # Discover device using Bleak
            scanner = BleakScanner()
            devices = await scanner.discover(return_adv=True)

            # Find our device
            device_found = False
            for device, adv_data in devices.values():
                if device.address.lower() == self.address.lower():
                    device_found = True
                    break

            if not device_found:
                raise UpdateFailed(f"Device {self.address} not found")

            # Connect and read data
            async with BleakClient(self.address) as client:
                if not client.is_connected:
                    raise UpdateFailed(f"Could not connect to {self.address}")

                # For now, return mock data
                # In a production implementation, you would read actual BLE characteristics
                return {
                    "weight": 75.5,
                    "fat_percentage": 20.5,
                    "muscle_mass": 55.2,
                    "water_percentage": 60.5,
                    "bone_mass": 2.8,
                    "basal_metabolism": 1600,
                    "bmi": 25.5,
                }

        except Exception as err:
            raise UpdateFailed(f"Error reading BLE scale: {err}") from err


class BLEScaleSensorEntity(CoordinatorEntity, SensorEntity):
    """Representation of a BLE Scale sensor."""

    entity_description: BLEScaleSensorEntityDescription

    def __init__(
        self,
        coordinator: BLEScaleDataUpdateCoordinator,
        entry: ConfigEntry,
        description: BLEScaleSensorEntityDescription,
    ) -> None:
        """Initialize the sensor entity."""
        super().__init__(coordinator)
        self.entity_description = description
        self._attr_unique_id = f"{entry.data[CONF_ADDRESS]}_{description.key}"
        self._attr_device_name = entry.data[CONF_NAME]

    @property
    def native_value(self) -> float | None:
        """Return the native value of the sensor."""
        if self.coordinator.data and self.entity_description.metric_key:
            return self.coordinator.data.get(self.entity_description.metric_key)
        return None
