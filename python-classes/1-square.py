#!/usr/bin/python3
"""
    This module creates a square class with
    a single private attribute.
"""


class Square:
    """
        This is a square class, now it initalizes
        the private attribute of size
        (int) __size: Square's size. 
    """
    def __init__(self, size):
        self.__size = size