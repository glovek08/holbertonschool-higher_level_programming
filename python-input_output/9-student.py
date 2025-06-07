#!/usr/bin/python3
"""
Module that defines a Student class.
"""


class Student:
    def __init__(self, first_name: str = "n/a",
                 last_name: str = "n/a",
                 age: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
