#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if matrix[i]:
            print("{}".format(' '.join(map(str, matrix[i]))), end='')
            print('')
    if not matrix or not matrix[-1]:
        print('')
