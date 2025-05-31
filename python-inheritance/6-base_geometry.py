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

# base1 = BaseGeometry()
# base1.area()
