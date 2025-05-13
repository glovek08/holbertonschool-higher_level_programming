#!/usr/bin/python3
matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
def print_matrix_integer(matrix=[[]]):
    matrix_len = len(matrix)
    i = 0
    for outer in matrix:
        if (i != matrix_len):
            for inner in matrix[i]:
                if (matrix[i].index(inner) + 1 != len(matrix[i])):
                    print("{:d}".format(inner), end=' ')
                else:
                    print("{:d}".format(inner), end='')
        print()
        i += 1
print_matrix_integer(matrix)