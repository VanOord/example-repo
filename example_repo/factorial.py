"""Factorial function."""


def fact(n):
    """Factorial function."""

    if isinstance(n, (float, int)) is not True:
        return "invalid input type"

    if n > 0:
        return n * fact(n - 1)
    else:
        return 1
