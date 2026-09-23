#!/usr/bin/python3
"""Divide matrix elements."""


def matrix_divided(matrix, div):
    """Return a new matrix divided by div."""
    if (not isinstance(matrix, list) or not matrix or
            any(not isinstance(row, list) for row in matrix) or
            any(not row for row in matrix) or
            any(not isinstance(n, (int, float)) or isinstance(n, bool)
                for row in matrix for n in row)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    if any(len(row) != len(matrix[0]) for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(n / div, 2) for n in row] for row in matrix]
