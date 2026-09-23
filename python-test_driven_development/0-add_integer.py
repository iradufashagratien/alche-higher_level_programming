#!/usr/bin/python3
"""Add two integers."""


def add_integer(a, b=98):
    """Return the sum of two integers or floats."""
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
