#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if matrix[i]:
            print(' '.join(map(str, matrix[i])), end='')
        if i != len(matrix) - 1 and i + 1 < len(matrix):
            print('$')
        else:
            print('$')
    else:
        print('$')
