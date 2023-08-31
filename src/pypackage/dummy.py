"""Dummy module."""


def dummy_1(*dummy: bool) -> str:
    """Return the string dummy-1."""
    return "dummy-1" if dummy else "duh"


def dummy_2(*dummy: bool) -> str:
    """Return the string dummy-2."""
    return "dummy-2" if dummy else "duh"
