#!/usr/bin/python3
"""Defines a class MyList that inherits from list."""


class MyList(list):
    """MyList class - a list with a sorted-print method."""

    def print_sorted(self):
        """Print the list, but sorted in ascending order."""
        print(sorted(self))
