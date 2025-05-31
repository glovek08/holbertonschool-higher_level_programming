#!/usr/bin/python3
"""
Module that defines an BaseGeometry class that validates input but does
nothing else.
"""


class BaseGeometry:
    """
    Empty class
    """
    def area(self):
        raise Exception(f"{self.area.__name__}() is not implemented")

    def integer_validator(self, name: str, value: int):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        self.__name = name
        self.__value = value

class Rectangle(BaseGeometry):
    def __init__(self, width: int, height: int):
        self.integer_validator("width", width)
        self.integer_validator("height", height)
