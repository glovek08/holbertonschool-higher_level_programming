#!/usr/bin/python3
"""
Module that extends the Student class and
gives it the functionality to filter down
the JSON string.
"""
Student = __import__("9-student").Student


class Student(Student):
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
