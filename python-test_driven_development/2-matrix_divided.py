#!/usr/bin/python3

"""
    This module divides a matrix aosdkosakdkqwed
    asodaspdkqw
    asdokapwiokdiopawpoidad Who the actual fuck writes this kind of
    doc nowadays!!??
"""


def matrix_divided(matrix, div):
    """
        Divides the elements of the matrix by a given divisor.
        Divisor must be either int or float.

        matrix: 2-D list of int or float elements.
        div: the divisor.

        Raises TypeError if the matrix doesn't contain int or float,
               or if div is not a number, or if the rows are not of equal size.
        Raises ZeroDivisionError if div is zero.
    """
    if not isinstance(matrix, list) or not all(
            isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists)\
            of integers/floats")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not matrix:
        pass
    row_length = 0
    if matrix and len(matrix) > 0:
        row_length = len(matrix[0])
    new_matrix = []
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix\
                (array of arrays of integers/floats)")

        if len(row) != row_length and matrix:
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []
        for column in row:
            if not isinstance(column, (int, float)):
                raise TypeError("matrix must be a matrix\
                    (array of arrays of integers/floats)")
            new_row.append(round(column / div, 2))
        new_matrix.append(new_row)

    return new_matrix
