#!/usr/bin/python3
"""
This module defines a square class that uses the Rectangle base class
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Creates a Square object using Rectangle as the parent class
    and BaseGeometry as the base class.
    Attributes:
        (int) size: the size of the square
    """

    def __init__(self, size: int):
        self.integer_validator("size", size)
        self.__size = size

    def area(self) -> int:
        return self.__size ** 2

    def __str__(self) -> str:
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

# my_square = Square(12)
# print(my_square)
