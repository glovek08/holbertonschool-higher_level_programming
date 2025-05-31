#!/usr/bin/python3
"""
Module that defines an empty BaseGeometry class.
"""


class BaseGeometry:
    """
    Empty class
    """
    def area(self):
        raise Exception(f"{self.area.__name__}() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{value} must be greater than 0")
        self.name = name
        self.value = value

# base1 = BaseGeometry()
# base1.area()