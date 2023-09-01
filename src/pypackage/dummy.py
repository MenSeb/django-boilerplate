"""Dummy module."""

from __future__ import annotations


def dummy_1(*, dummy: bool = False) -> str:
    """Return the string dummy-1."""
    if dummy:
        return "dummy-1"

    return "duh"


def dummy_2(*, dummy: bool = False) -> str:
    """Return the string dummy-2."""
    if dummy:
        return "dummy-2"

    return "duh"


def dummy_3(*, dummy: bool = False) -> str:
    """Return the string dummy-3."""
    if dummy:
        return "dummy-3"

    return "duh"
