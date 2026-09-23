#!/usr/bin/python3
"""Print a square."""


def print_square(size):
    """Print a square using #."""
    if not isinstance(size, int) or isinstance(size, bool):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
