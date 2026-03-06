"""Tests for rapid-timer-decorator."""

import pytest
from rapid_timer_decorator import decorator


class TestDecorator:
    """Test suite for decorator."""

    def test_basic(self):
        """Test basic usage."""
        result = decorator("test")
        assert result is not None

    def test_empty(self):
        """Test with empty input."""
        try:
            decorator("")
        except (ValueError, TypeError):
            pass  # Expected for some utilities

    def test_type_error(self):
        """Test with wrong type raises or handles gracefully."""
        try:
            result = decorator(12345)
        except (TypeError, AttributeError, ValueError):
            pass  # Expected for strict-typed utilities
