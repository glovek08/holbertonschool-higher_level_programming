#!/usr/bin/python3
"""
This module contains a locked class that prevents new properties
not defines in __slots__
"""


class LockedClass:
    __slots__ = "first_name"
