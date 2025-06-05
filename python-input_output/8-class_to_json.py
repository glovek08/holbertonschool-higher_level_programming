#!/usr/bin/python3
"""
I'll deal with documentation later
"""
import json


class Country:
    def __init__(self, name: str, department):
        self.__name = name
        self.__departments = [department]

    @property
    def departments(self) -> list:
        return self.__departments

    @departments.setter
    def departments(self, value):
        self.__departments.append(value)

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def to_dict(self):
        return {
            "name": self.__name,
            "departments": self.__departments
        }

    def toJSON(self):
        return self.to_dict()


uruguay = Country("Uruguay", "Montevideo")
# print(uruguay.__dict__)
uruguay.departments = "Canelones"
# print(uruguay.departments)
# print(uruguay.__dict__)


def class_to_json(obj):
    if hasattr(obj, 'to_dict') and callable(getattr(obj, 'to_dict')):
        print(json.dumps(obj.to_dict(), sort_keys=True, indent=4))
    else:
        print(json.dumps(obj, sort_keys=True, indent=4))
    # print(json.dumps(obj.__dict__, sort_keys=True))


class_to_json(uruguay)
