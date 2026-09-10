#!/usr/bin/python3
"""Defines a class MyInt that inherits from int."""


class MyInt(int):
    """MyInt class - a rebel int with == and != inverted."""

    def __eq__(self, other):
        """Invert the behavior of the == operator."""
        return int(self) != int(other)

    def __ne__(self, other):
        """Invert the behavior of the != operator."""
        return int(self) == int(other)
