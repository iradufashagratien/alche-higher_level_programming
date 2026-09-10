#!/usr/bin/python3
"""Module that defines the BaseGeometry class with an area method."""


class BaseGeometry:
    """Base class for geometry shapes."""

    def area(self):
        """Raise an Exception since area() is not implemented."""
        raise Exception("area() is not implemented")
