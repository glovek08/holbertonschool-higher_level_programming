#!/usr/bin/python3
"""
Module that defines a class for creating geometric objects
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    Creates a rectangle
    """
    def __init__(self, width: int, height: int):
        """
        Initialize rectangle with width and height
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    # def area(self):
    #     return self.__height * self.__width

# print(issubclass(Rectangle, BaseGeometry))
