# Configuration Examples

## Basic Configuration (GUI)

The easiest way to configure the BLE Scale integration is through the Home Assistant UI:

1. Go to **Settings** → **Devices & Services** → **Integrations**
2. Click **Create Integration**
3. Search for **BLE Scale**
4. Follow the setup wizard and select your scale

## Multiple Scales

You can add multiple scales by repeating the setup process for each device:

1. Each scale will get a unique device name
2. Entities will be created for each scale with appropriate naming
3. All scales will update on the same polling interval

Example with two scales:

- Scale 1 (Bedroom): `sensor.bedroom_weight`, `sensor.bedroom_fat_percentage`, etc.
- Scale 2 (Bathroom): `sensor.bathroom_weight`, `sensor.bathroom_fat_percentage`, etc.

## Scale Model Selection

When setting up a scale, you can choose:

- **Auto**: Automatic detection (recommended if your scale is supported)
- **Specific Model**: Select your exact scale model from the list

## Supported Models

See [README.md](README.md#supported-scale-models) for the full list of supported scale models.

## Using with Bluetooth Proxies

If you have Bluetooth proxies configured:

1. The integration will automatically use available proxies
2. Proxies extend the range of Bluetooth connectivity
3. Multiple proxies can work together for better coverage

To set up Bluetooth proxies in Home Assistant:

1. Go to **Settings** → **Devices & Services** → **Bluetooth**
2. Configure your Bluetooth proxy devices
3. The BLE Scale integration will automatically use them

## Update Interval

The default polling interval is 5 minutes. The scale will only send new data when a fresh measurement is taken (i.e., when someone steps on it).

If you need to change the update interval, you can do so in the integration options after adding it.
