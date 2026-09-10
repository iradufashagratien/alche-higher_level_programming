#!/usr/bin/python3
"""Module that defines a class MyList that inherits from list."""


class MyList(list):
    """Class that represents a list with an additional sorted print."""

    def print_sorted(self):
        """Print the list in ascending sorted order."""
        print(sorted(self))
