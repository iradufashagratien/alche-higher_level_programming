#!/usr/bin/python3
"""Module that safely divides two integers."""


def safe_print_division(a, b):
    """Divide a by b, print the result, and return it (or None)."""
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        result = None
    finally:
        print("Inside result: {}".format(result))
    return result
