#!/usr/bin/python3
"""
Defines a function to check whether or not an object is exactly the same class
"""


def is_same_class(obj, a_class):
    """
    Checks if given object is exactly an instance of a given class
    Arguments:
        obj = given object
        a_class = the class that should be the exact type of @obj
    Return:
        True: if @obj is exactly an instance of @a_class (not inherited)
        False: otherwise
    """
    return type(obj) is a_class
