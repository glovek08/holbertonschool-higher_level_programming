#!/usr/bin/python3
"""
This module re-implements the Student class to change its
attributes from a json file.
"""


class Student():
    def __init__(self, first_name: str = "n/a",
                 last_name: str = "n/a",
                 age: int = 0):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for attr in attrs:
            if hasattr(self, attr):
                my_dict[attr] = getattr(self, attr)
        return my_dict

    def reload_from_json(self, json: dict):
        for key, value in json:
            self.__dict__[key] = value
