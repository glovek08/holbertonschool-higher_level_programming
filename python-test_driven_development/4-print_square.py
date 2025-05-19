#!/usr/bin/python3
"""
    This module is now well documented.
"""
def print_square(size: int = 0):
    """
        This documentation is excellent.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        row_string = "#" * size
        print(row_string)
