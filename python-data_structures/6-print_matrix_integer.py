#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i in range(len(matrix)):
        if matrix[i]:
            print("{}".format(' '.join(map(str, matrix[i]))), end='')
            print('')
    if not matrix or not matrix[-1]:
        print('')
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()
