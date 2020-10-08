"""Factorial function."""


def fact(n):
    """Factorial function."""

    if n > 0:
        return n * fact(n - 1)
    else:
        return 1
