#!/usr/bin/python3
"""
Module that defines a function for attribute setting.
"""


def add_attribute(an_obj: object, attr: str, value: int):
    """
    Function that tries to set a new attribute to a given object
    Arguments:
        an_obj: target object.
        attr: specified attribute to add.
        value: attr's data.
    Raises:
        TypeError: if new attribute coulnd't be added.
    """
    if not isinstance(value, int):
        raise TypeError("can't add new attribute")
    if not hasattr(an_obj, '__dict__'):
        if not hasattr(an_obj, attr):
            raise TypeError("can't add new attribute")
    setattr(an_obj, attr, value)

class Mamacita:
    def __init__(self, rand):
        self.rand = rand

uy = Mamacita("Sexy")
print(uy.rand)
add_attribute(uy, "edad", 29)
print(uy.edad)
# add_attribute(uy, "is_traba", "yes")
# print(uy.is_traba)
print(uy.__dict__)