"""Tests for the API module."""

import pytest

from txtstats import text_stats


def test_text_stats():
    """Test text_stats() function for expected output."""
    d = text_stats("Hello world!")
    assert isinstance(d, dict)

    for key in d:
        assert isinstance(key, str)


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
