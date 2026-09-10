#!/usr/bin/python3
"""Defines a function that returns a dict description of an object."""


def class_to_json(obj):
    """Return the dictionary description of a simple-data-structure object.

    Args:
        obj: an instance of a class whose attributes are all
            serializable (list, dict, str, int, bool).

    Returns:
        dict: the attribute dictionary of obj.
    """
    return obj.__dict__
