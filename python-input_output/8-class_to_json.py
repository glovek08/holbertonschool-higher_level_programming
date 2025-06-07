#!/usr/bin/python3
"""
I'll deal with documentation later
"""

# obj2 = MyClass2('Pedro', 65)

# print(obj2.__dict__)


def class_to_json(obj):
    return obj.__dict__

# class_to_json(uruguay)
# class Country:
#     def __init__(self, name: str, department):
#         self.__name = name
#         self.__departments = [department]

#     @property
#     def departments(self) -> list:
#         return self.__departments

#     @departments.setter
#     def departments(self, value):
#         self.__departments.append(value)

#     @property
#     def name(self) -> str:
#         return self.__name

#     @name.setter
#     def name(self, value):
#         self.__name = value

#     def to_dict(self):
#         return {
#             "name": self.__name,
#             "departments": self.__departments
#         }

    # def toJSON(self):
    #     return self.to_dict()


# uruguay = Country("Uruguay", "Montevideo")
# print(uruguay.__dict__)
# uruguay.departments = "Canelones"
# print(uruguay.departments)
# print(uruguay.__dict__)

# class CustomEncoder(json.JSONEncoder):
#     def deault(self, obj):
#         if isinstance(obj, MyClass):
#             return {
#                 'name': obj.name,
#                 'number': obj.number,
#             }
#             return json.JSONEncoder.default(self, obj)
