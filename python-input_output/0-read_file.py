#!/usr/bin/python3
"""Defines a function that reads a text file and prints it to stdout."""


def read_file(filename=""):
    """Read a UTF8 text file and print its content to stdout.

    Args:
        filename (str): the path of the file to read.
    """
    with open(filename, "r", encoding="utf-8") as f:
        print(f.read(), end="")
