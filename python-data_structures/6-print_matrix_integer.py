#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    [print(' '.join(["{:d}".format(num) for num in row])) for row in matrix]
