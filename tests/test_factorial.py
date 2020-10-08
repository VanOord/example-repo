"""Test function for the factorial function."""

from example_repo.factorial import fact


def test_fact():
    """Test function for the factorial function."""

    assert fact(2) == 2
    assert fact(0) == 1
    assert fact("0") == "invalid input type"
