# BLE Scale - Home Assistant Integration

A Home Assistant custom integration for BLE Smart Scales, providing seamless reading of body composition data from 23+ BLE scale brands with support for Bluetooth proxies.

## Features

- **Multi-brand support**: Works with Xiaomi, Renpho, Eufy, Yunmai, Beurer, Sanitas, Medisana, and 15+ other scale brands
- **Bluetooth Proxy support**: Works with Home Assistant Bluetooth proxies for extended range and better reliability
- **Rich body composition metrics**: Weight, body fat %, muscle mass, water %, bone mass, basal metabolism, BMI
- **Easy configuration**: User-friendly GUI configuration in Home Assistant
- **Automatic discovery**: Discovers scales via Bluetooth automatically
- **Real-time updates**: Periodic polling from your BLE scales
- **Local-first**: All data processing happens locally on your Home Assistant instance

## Installation

### HACS (Recommended)

1. Open HACS in your Home Assistant instance
2. Go to "Integrations"
3. Click the "Create" button
4. Search for "BLE Scale"
5. Click on the BLE Scale integration
6. Click "Install"
7. Restart Home Assistant

### Manual Installation

1. Download the integration from [GitHub](https://github.com/KristianP26/ble-scale-hass/releases)
2. Extract to `custom_components/ble_scale` in your Home Assistant configuration directory
3. Restart Home Assistant

## Configuration

### Through GUI

1. Go to Settings → Devices & Services
2. Click "Create Automation" or "Create Integration"
3. Search for "BLE Scale"
4. Follow the setup wizard:
   - Select your scale's Bluetooth address
   - Name your scale
   - Choose the scale model (or "auto" for automatic detection)

### Supported Scale Models

The integration supports the following models:

- **Xiaomi**: Mi Scale 2, Body Composition Scale, Scale Pro
- **Renpho**: Smart Scale
- **Eufy**: Smart Scale
- **Yunmai**: Mini, M8
- **Beurer**: BF 800, BF 900
- **Sanitas**: SFB 912
- **Medisana**: BS 445
- **Withings**: Body Scale
- **Nokia**: Body Scale
- **Fitbit**: Aria, Aria 2
- **Garmin**: Index
- **Honor**: Scale
- **Realme**: Scale
- **Tefal**: Scale
- **Umami**: Scale
- **Haeno**: Scale
- **Picooc**: Scale

Plus automatic detection mode for compatible scales.

## Provided Entities

For each configured scale, the following sensor entities are created:

- `sensor.<scale_name>_weight` - Current weight in kg
- `sensor.<scale_name>_fat_percentage` - Body fat percentage
- `sensor.<scale_name>_muscle_mass` - Muscle mass in kg
- `sensor.<scale_name>_water_percentage` - Water percentage
- `sensor.<scale_name>_bone_mass` - Bone mass in kg
- `sensor.<scale_name>_basal_metabolism` - Basal metabolic rate in kcal
- `sensor.<scale_name>_bmi` - Body Mass Index

## Bluetooth Proxy Support

This integration fully supports Home Assistant's Bluetooth proxy feature, which allows you to:

- Extend the range of Bluetooth devices
- Use multiple Bluetooth adapters
- Improve reliability in multi-storey homes

The integration will automatically use available Bluetooth proxies if configured in your Home Assistant setup.

## Troubleshooting

### Scale not discovered

- Ensure your scale is powered on and in pairing mode
- Check that Bluetooth is enabled on your Home Assistant instance
- Try restarting the Bluetooth service: Settings → System → Hardware → Bluetooth

### No data being read

- Verify the scale model is correctly selected (try "auto" if unsure)
- Check Home Assistant logs for error messages
- Ensure the scale has a fresh reading (step on scale to trigger new measurement)
- Verify Bluetooth connection strength in proximity

### Connection timeout

- Move closer to the scale or Home Assistant device
- Use a Bluetooth proxy if available
- Check for interference from other Bluetooth devices
- Increase the update interval in advanced settings

## Contributing

Contributions are welcome! To add support for new scale models:

1. Fork the [repository](https://github.com/KristianP26/ble-scale-hass)
2. Add your scale's BLE characteristics to `custom_components/ble_scale/scales/`
3. Test with your device
4. Submit a pull request

## Based On

This integration is built on top of [ble-scale-sync](https://github.com/KristianP26/ble-scale-sync), a universal BLE smart scale bridge by Kristian Partl.

## License

GPL-3.0 - See [LICENSE](LICENSE) for details

## Credits

- [ble-scale-sync](https://github.com/KristianP26/ble-scale-sync) for scale protocol implementations
- [openScale](https://github.com/oliexdev/openScale) for scale adaptation code
- [Home Assistant](https://www.home-assistant.io/) for the amazing open-source platform
