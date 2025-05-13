#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    i = 0
    for outer in matrix:
        if (i != matrix_len):
            for inner in matrix[i]:
                print("{el:d}".format(el = inner), end=' ')
        print()
        i += 1
