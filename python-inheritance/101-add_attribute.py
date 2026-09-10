#!/usr/bin/python3
"""Defines a function that adds an attribute to an object, if allowed."""


def add_attribute(obj, name, value):
    """Add a new attribute to an object, if it's allowed.

    Args:
        obj: the object to add the attribute to.
        name (str): the name of the new attribute.
        value: the value of the new attribute.

    Raises:
        TypeError: if the object can't have new attributes.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
