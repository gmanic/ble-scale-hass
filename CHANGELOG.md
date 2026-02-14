# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [1.0.0] - 2026-02-14

### Added

- Initial release of BLE Scale Home Assistant integration
- Support for 23+ BLE smart scale brands
- GUI configuration via Home Assistant UI
- Bluetooth proxy support for extended range
- Rich body composition metrics (weight, fat %, muscle mass, water %, bone mass, metabolism, BMI)
- Automatic scale discovery via Bluetooth
- Real-time sensor entities with periodic polling
- HACS support for easy installation

### Features

- Automatic Bluetooth device discovery
- Per-scale configuration
- Support for manual scale model selection or automatic detection
- Local data processing (no cloud dependencies)
- Full type hints for Python 3.11+
