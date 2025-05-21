#!/usr/bin/python3
"""
    This module defines a square class.
"""


class Square:
    """
        Represents a square with a given size.

        Attributes:
            __size (int): The size of the square's side. Must be >= 0.
    """
    def __init__(self, size: int = 0):
        self.size(size)

    def size(self):
        return self.__size

    def size(self, value: int = 0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif (size < 0):
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self) -> int:
        """
            Calculates the area of the square.

            Returns:
                int: The area of the square.
        """
        return self.__size * self.__size
