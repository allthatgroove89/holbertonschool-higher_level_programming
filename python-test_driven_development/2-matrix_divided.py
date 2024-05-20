#!/usr/bin/python3

def matrix_divided(matrix, div):
    # Check if div is an integer or a floar, otherwise
    # TypeError
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    # Check if div is zero, otherwise raise a TypeError
    if div == 0:
        raise TypeError("division by zero")
    # Check if matrix is a list of lists of
    # integers or floats, otherwise raise a TypeError
    if isinstance(matrix, (int, float)):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats")
    # Check if all rows in the matrix have the same size,
    # otherwise raise a TypeError
    if not all(len(row) == len(matrix[0])for row in matrix):
        raise TypeError("Each row of the matrix must ahve the same size")
    # Divide each element in the matrix by div and round to 2 decimal places
    result = [[round(element / div, 2) for element in row] for row in matrix]
    # Return the resulting matrix
    return result
