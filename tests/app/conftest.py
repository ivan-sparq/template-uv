import pytest


@pytest.fixture
def example() -> str:
    """Provide a simple string fixture for template tests."""
    return "example"
