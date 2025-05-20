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
        """
            Initializes a Square instance.

            Args:
                size (int): The size of the square's side. Defaults to 0.

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
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
