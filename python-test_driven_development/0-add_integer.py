#!/usr/bin/python3
"""Add two integers together and return the result.
"""


def add_integer(a, b=98):
    """Add two integers or floats after converting them to integers."""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
