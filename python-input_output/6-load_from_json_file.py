#!/usr/bin/python3
"""Defines a function that creates an object from a JSON file."""
import json


def load_from_json_file(filename):
    """Create and return an object from the content of a JSON file.

    Args:
        filename (str): the path of the JSON file to read.

    Returns:
        The Python data structure represented in the file.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
