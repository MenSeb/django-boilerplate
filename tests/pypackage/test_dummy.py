"""Test dummy module."""


from pypackage.dummy import dummy_1, dummy_2


def test_dummy_1() -> None:
    """Test dummy function."""
    assert dummy_1() == "duh"
    assert dummy_1(dummy=False) == "duh"
    assert dummy_1(dummy=True) == "dummy-1"


def test_dummy_2() -> None:
    """Test dummy function."""
    assert dummy_2(dummy=False) == "duh"
    assert dummy_2(dummy=True) == "dummy-2"
