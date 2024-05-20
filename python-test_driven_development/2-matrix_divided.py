#!/usr/bin/python3

def matrix_divided(matrix, div):
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise TypeError("division by zero")
    if isinstance(matrix, (int, float)):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    if not all(len(row) == len(matrix[0])for row in matrix):
        raise TypeError("Each row of the matrix must ahve the same size")
    result = [[round(element / div, 2 ) for element in row] for row in matrix]
    return result
