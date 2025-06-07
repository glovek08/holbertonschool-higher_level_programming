#!/usr/bin/python3
"""
Module that extends the Student class and
gives it the functionality to filter down
the JSON string.
"""


class Student(Student):
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

# student1 = Student('Jefe', 'Color', 25)
# print(student1.to_json(["first_name"]))
