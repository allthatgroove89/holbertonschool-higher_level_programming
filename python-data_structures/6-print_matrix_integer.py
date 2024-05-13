#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if matrix[i]:
            print("{}".format(' '.join(map(str, matrix[i]))))
    if not matrix or not matrix[-1]:
        print('')
