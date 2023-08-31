"""Test dummy module."""

from pypackage.dummy import dummy_1, dummy_2


def test_dummy_1() -> None:
    """Test dummy function."""
    dummy_string = dummy_1()
    assert dummy_string == "duh"


def test_dummy_2() -> None:
    """Test dummy function."""
    dummy_string = dummy_2()
    assert dummy_string == "duh"
