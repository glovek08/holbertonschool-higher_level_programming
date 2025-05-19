#!/usr/bin/python3
"""
Module for printing a square with the character #.

This module contains the function `print_square` which prints a square of a given size. It validates input and raises appropriate exceptions.
""" 
def print_square(size: int = 0):
    """
        Receives an size which is type int, otherwise raises TypeError
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        print("", end="")
        return
    for i in range(size):
        row_string = "#" * size
        print(row_string)
