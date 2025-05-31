#!/usr/bin/python3
"""
Module that defines a function to check if an object is an instance of,
or inherited from, a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.
        Arguments:
        obj = given object
        a_class = the class that should be the exact type of @obj
    Return:
        True: if @obj is kind of an instance of @a_class
        False: otherwise
    """
    return True if isinstance(obj, a_class) else False
