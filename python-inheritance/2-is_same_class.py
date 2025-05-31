#!/usr/bin/python3
"""
Defines a function to check wether or not an object instance of a class
"""
def is_same_class(obj, a_class):
    """
    Checks if given object is an instance of a given class
    Arguments:
        obj = given object
        a_class = the class that should be parent of @obj
    Return:
        True: if @obj is an instance of @a_class
    """
    return True if isinstance(obj, a_class) else False