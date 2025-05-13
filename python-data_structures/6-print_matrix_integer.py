#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    for outer in range(matrix_len):
        row = matrix[outer]
        row_length = len(row)
        for inner in range(row_length):
            print("{:d}".format(row[inner]), end='')
            if inner != row_length - 1:
                print(" ", end='')
        print()
