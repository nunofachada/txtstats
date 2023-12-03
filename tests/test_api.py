"""Tests for the API module."""

import pytest

from txtstats import text_stats


def test_text_stats_output_type(string_to_test):
    """Test text_stats() function for expected output type."""
    d = text_stats(string_to_test)

    # Check that d is a dictionary
    assert isinstance(d, dict)
    # Check that all keys in d are of type string
    assert {type(k) for k in d} == {str}


def test_text_stats_errors():
    """Test text_stats() function for expected errors."""
    with pytest.raises(TypeError):
        text_stats(1)

    with pytest.raises(TypeError):
        text_stats(1.34)

    with pytest.raises(TypeError):
        text_stats(["hello", "world"])

    with pytest.raises(TypeError):
        text_stats(("hello", "world", 1, 2, 3))
