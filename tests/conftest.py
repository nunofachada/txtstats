"""Centralized tests configurations and fixtures."""

import pytest


@pytest.fixture()
def string_to_test():
    """Fixture that defines the string to be tested in the API tests."""
    return "Hello world!"
