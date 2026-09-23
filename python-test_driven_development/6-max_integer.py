#!/usr/bin/python3
"""Find the maximum integer."""


def max_integer(list=[]):
    """Return the maximum integer or None."""
    if len(list) == 0:
        return None
    result = list[0]
    i = 1
    while i < len(list):
        if list[i] > result:
            result = list[i]
        i += 1
    return result
