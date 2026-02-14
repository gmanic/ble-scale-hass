# Contributing

Contributions are welcome and greatly appreciated! This document provides guidelines and instructions for contributing to the BLE Scale Home Assistant integration.

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

- **Use a clear and descriptive title**
- **Describe the exact steps which reproduce the problem**
- **Provide specific examples to demonstrate the steps**
- **Describe the behavior you observed after following the steps**
- **Explain which behavior you expected to see instead and why**
- **Include screenshots and animated GIFs if possible**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

- **Use a clear and descriptive title**
- **Provide a step-by-step description of the suggested enhancement**
- **Provide specific examples to demonstrate the steps**
- **Describe the current behavior and expected behavior**

### Pull Requests

- Follow the Python style guide (PEP 8)
- Include appropriate test cases
- Update documentation as needed
- End all files with a newline
- Use type hints throughout

## Development Setup

1. Clone the repository:
   ```bash
   git clone https://github.com/JustBeanie/ble-scale-hass
   cd ble-scale-hass
   ```

2. Install development dependencies:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. Create a branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```

4. Make your changes and ensure tests pass:
   ```bash
   pytest
   ruff check .
   ruff format .
   mypy custom_components/ble_scale
   ```

5. Commit with clear messages:
   ```bash
   git commit -m "Add feature: description of changes"
   ```

6. Push and create a pull request

## Adding Support for New Scale Models

To add support for a new scale model:

1. Research the scale's BLE service and characteristic UUIDs
2. Create a new file in `custom_components/ble_scale/scales/` following the existing pattern
3. Implement the `ScaleAdapter` interface
4. Add the model to `const.py` in the `SCALE_MODELS` list
5. Test with an actual device if possible
6. Update `README.md` with the new model
7. Submit a pull request with details about the scale

## Testing

Run tests with:
```bash
pytest tests/
```

With coverage:
```bash
pytest tests/ --cov=custom_components/ble_scale
```

## Code Style

This project uses:
- **ruff** for linting and formatting
- **mypy** for type checking

Run these checks:
```bash
ruff check custom_components/ble_scale
ruff format custom_components/ble_scale
mypy custom_components/ble_scale
```

## Commit Messages

Use clear, descriptive commit messages:
- Use the imperative mood ("Add feature" not "Added feature")
- Use the past tense for changes ("Changed behavior" not "Changes behavior")
- Limit the first line to 72 characters
- Reference issues and pull requests liberally after the first line

## License

By contributing, you agree that your contributions will be licensed under the GPL-3.0 License.
