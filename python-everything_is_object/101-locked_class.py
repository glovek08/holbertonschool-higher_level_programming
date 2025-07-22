#!/usr/bin/python3
"""
This module contains a locked class that prevents the user
fram dynamically creating new instance attributes,
except for 'first_name'.
"""


class LockedClass:
    """
    A class with restricted attributes. Only 'first_name' can be set.
    Any attempt to set other attributes will raise an AttributeError.
    """

    __slots__ = ("first_name",)
