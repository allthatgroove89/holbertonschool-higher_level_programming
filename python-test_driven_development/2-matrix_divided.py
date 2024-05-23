#!/usr/bin/python3
"""
Task: 2-matrix_divided
Test: Cases for unittest
Args: matrix, div
"""


def matrix_divided(matrix, div):
    """Divide a Matrix by two
    >>> matrix = [[1, 2, 3], [4, 5, 6]]
    >>> matrix_divided(matrix, 3)
    [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
    >>> matrix_divided(matrix, -2)
    [[-0.5, -1.0, -1.5], [-2.0, -2.5, -3.0]]
    >>> matrix = [[4, 5, 0]]
    >>> matrix_divided(matrix, 1)
    [[4.0, 5.0, 0.0]]
    >>> matrix = [[3, "9"], [15, 3]]
    matrix_divided(matrix, 3)
    TypeError: matrix must be a matrix (array of arrays of integers/floats)
    """
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix\
            (list of lists) of integers/floats")
    size = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix\
                (list of lists) of integers/floats")
        if size is None:
            size = len(row)
        elif size != len(row):
            raise TypeError("Each row of the matrix must have the same size")
        for num in row:
            if not isinstance(num, (int, float)):
                raise TypeError("matrix must be a matrix\
                    (list of lists) of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(element / div, 2) for element in row] for row in matrix]
