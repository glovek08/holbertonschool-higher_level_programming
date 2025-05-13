#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    for outer in range(len(matrix)):
        row = matrix[outer]
        for inner in range(len(row)):
            print("{:d}".format(row[inner]), end='')
            if inner != len(row) - 1:
                print(" ", end='')
        print()
