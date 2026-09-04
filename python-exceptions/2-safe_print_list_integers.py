#!/usr/bin/python3
"""Module that safely prints only the integers found in a list."""


def safe_print_list_integers(my_list=[], x=0):
    """Print the first x elements of my_list that are integers."""
    count = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            count += 1
        except (TypeError, ValueError):
            continue
    print()
    return count
