"""Tests for BLE Scale config flow."""
import pytest
from homeassistant.const import CONF_ADDRESS, CONF_NAME
from custom_components.ble_scale.config_flow import BLEScaleConfigFlow
from custom_components.ble_scale.const import CONF_SCALE_MODEL


@pytest.mark.asyncio
async def test_step_user():
    """Test user step."""
    flow = BLEScaleConfigFlow()
    
    user_input = {
        CONF_ADDRESS: "AA:BB:CC:DD:EE:FF",
        CONF_NAME: "Test Scale",
        CONF_SCALE_MODEL: "xiaomi_scale_2",
    }
    
    # Mock the async_set_unique_id and _abort_if_unique_id_configured methods
    flow.async_set_unique_id = lambda x: None
    flow._abort_if_unique_id_configured = lambda: None
    
    result = await flow.async_step_user(user_input)
    
    assert result["type"] == "create_entry"
    assert result["title"] == "Test Scale"
    assert result["data"] == user_input
