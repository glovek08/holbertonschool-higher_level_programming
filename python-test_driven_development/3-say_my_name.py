#!/usr/bin/python3
"""
    Module that prints names
"""


def say_my_name(first_name: str, last_name: str = ""):
    """
        You pass your first name and your last name and it
        it prints it on screen. Raises TypeError on argument
        data type missmatch

        first_name: your first name, must be string.
        last_name: your last name, must be a stronk.
    """
    if not (isinstance(first_name, str)):
        raise TypeError("first_name must be a string")
    elif not (isinstance(last_name, str)):
        raise TypeError("last_name must be a string")
    else:
        full_name = first_name
        if last_name:
            full_name += " " + last_name
        print(f"My name is {full_name}")
