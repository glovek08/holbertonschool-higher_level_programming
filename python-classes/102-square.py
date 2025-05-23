#!/usr/bin/python3
"""
    This module defines a Square class.
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
                size (int): The size of the square. Must be an integer >= 0.

            Raises:
                TypeError: If size is not an integer.
                ValueError: If size is less than 0.
        """
        self.size = size

    def __int__(self):
        return self.area()
    def __eq__(self, other):
        return self.area() == other.area()
    def __lt__(self, other):
        return self.area() < other.area()
    def __le__(self, other):
        return self.area() <= other.area()

    @property
    def size(self) -> int:
        """
            Retrieves the size of the square.

            Returns:
                int: The current size of the square.
        """
        return self.__size

    @size.setter
    def size(self, value: int):
        """
            Sets the size of the square.

            Args:
                value (int): The new size value.

            Raises:
                TypeError: If value is not an integer.
                ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self) -> int:
        """
            Calculates the area of the square.

            Returns:
                int: The area of the square.
        """
        return self.__size * self.__size
