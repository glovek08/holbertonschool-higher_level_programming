#!/usr/bin/python3


"""
In this module we define a Fucking class and a shit object.
"""


class Fucking:
    """
    Fucking class doesn't do shit
    """
    pass


shit = Fucking()


def lookup(obj) -> list:
    """
    Returns a list of all methods of a given object, up to the core.
    """
    return dir(obj)

# print(lookup(shit))
