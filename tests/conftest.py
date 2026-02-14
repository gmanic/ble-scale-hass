"""Test configuration for BLE Scale integration."""
import pytest
from unittest.mock import patch, MagicMock
from homeassistant.const import CONF_ADDRESS, CONF_NAME

from custom_components.ble_scale.const import CONF_SCALE_MODEL


@pytest.fixture
def mock_scale_data():
    """Provide mock scale data."""
    return {
        "weight": 75.5,
        "fat_percentage": 20.5,
        "muscle_mass": 55.2,
        "water_percentage": 60.5,
        "bone_mass": 2.8,
        "basal_metabolism": 1600,
        "bmi": 25.5,
    }


@pytest.fixture
def config_entry_data():
    """Provide test config entry data."""
    return {
        CONF_ADDRESS: "AA:BB:CC:DD:EE:FF",
        CONF_NAME: "Test Scale",
        CONF_SCALE_MODEL: "xiaomi_scale_2",
    }
