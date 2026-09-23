#!/usr/bin/python3
"""Divide every element of a matrix by a given number.
"""


def matrix_divided(matrix, div):
    """Return a new matrix with every element divided and rounded."""
    if not isinstance(matrix, list) or not matrix:
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if any(not isinstance(value, (int, float))
           for row in matrix for value in row):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_size = len(matrix[0])
    if any(len(row) != row_size for row in matrix):
        raise TypeError(
            "Each row of the matrix must have the same size"
        )

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [[round(value / div, 2) for value in row] for row in matrix]
