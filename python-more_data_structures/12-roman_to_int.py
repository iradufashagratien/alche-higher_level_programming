#!/usr/bin/python3
"""Roman to integer module."""


def roman_to_int(roman_string):
    """Convert a Roman numeral to an integer."""
    if not isinstance(roman_string, str):
        return 0
    values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev = 0
    for char in reversed(roman_string):
        if char not in values:
            return 0
        value = values[char]
        if value < prev:
            total -= value
        else:
            total += value
            prev = value
    return total
