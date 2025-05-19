#!/usr/bin/python3

def print_square(size: int = 0):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        row_string = "#" * size
        print(row_string)
