#!/usr/bin/python3
"""
Module with function that reads from text file and outputes
to standard output
"""


def read_file(filename=""):
    """
    Read a text file specified with @filename using UTF-8 encoding.
    """
    with open(filename, encoding="utf-8") as a_file:
        for a_line in a_file:
            print(f"{a_line.rstrip()}")

# read_file("README.md")
