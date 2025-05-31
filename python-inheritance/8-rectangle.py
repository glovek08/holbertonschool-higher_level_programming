#!/usr/bin/python3
"""
Module that defines a class for creating geometric objects
"""


class BaseGeometry:
    """
    Creates geometric objects
    """
    def area(self):
        raise Exception(f"{self.area.__name__}() is not implemented")

    def integer_validator(self, name: str, value: int):
        """
        Validate that a given value is a positive integer
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return True


class Rectangle(BaseGeometry):
    """
    Creates a rectangle
    """
    def __init__(self, width: int, height: int):
        """
        Initialize rectangle with width and height
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    # def area(self):
    #     return self.__height * self.__width

# print(issubclass(Rectangle, BaseGeometry))
