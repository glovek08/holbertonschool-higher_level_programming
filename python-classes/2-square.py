#!/usr/bin/python3
"""
    This module defines a square class.
"""


class Square:
    """
        This class defines a square. It receives a size,
        which is of type int and must not be lower than 0,
        defaults to 0 if no value is given.

        (int) __size: Square's size.
    """
    def __init__(self, size: int = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size
