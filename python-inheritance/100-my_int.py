#!/usr/bin/python3
"""
This module is a torture device.
"""


class MyInt(int):
    """
    Rebel class made to torture mathematicians
    """
    def __eq__(self, obj2):
        return not (super().__eq__(obj2))
