#!/usr/bin/python3
"""
    This module returns the
    addition of two given arguments.
"""


def add_integer(a, b=98):
    """
        Function that returns the sum of 2 arguments.
        a: first number, must be int or float.
        b: second number, must be int or float.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
