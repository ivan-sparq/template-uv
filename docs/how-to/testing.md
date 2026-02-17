# How to test

## With VS Code

1. Run the tests with the `All Tests` launch configuration.

## From terminal

1. Run all tests with coverage: `uv run pytest`.
2. Run tests without coverage overhead: `uv run pytest --no-cov`.
3. Run one test file: `uv run pytest tests/app/test_cli.py`.
