#!/usr/bin/python3
"""Module that defines a function to look up object attributes."""


def lookup(obj):
    """Return the list of available attributes and methods of an object."""
    return dir(obj)
