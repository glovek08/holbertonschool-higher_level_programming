#!/usr/bin/python3
"""
Module that defines a custom class with serialization methods.
"""
import json
import pickle


class CustomObject:
    def __init__(self, name: str = "", age: int = 0, is_student: bool = False):
        self.name = name
        self.age = age
        self.is_student = is_student
    
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")
    
    def serialize(self, filename):
        if isinstance(filename, str):
            try:
                with open(filename, mode="wb") as a_file:
                    pickle.dump(self, a_file)
                return True  # Indicate success
            except (AttributeError, TypeError, pickle.PicklingError) as error:
                print(f"Object cannot be serialized: {error}")
                return None
            except (OSError, FileNotFoundError) as error:
                print(f"File operation failed: {error}")
                return None
            except Exception as error:
                print(f"Unexpected error: {error}")
                return None
    
    @classmethod
    def deserialize(cls, filename):
        if isinstance(filename, str):
            try:
                with open(filename, mode="rb") as a_file:
                    return pickle.load(a_file)
            except (AttributeError, TypeError, pickle.PicklingError) as error:
                print(f"Object cannot be deserialized: {error}")
                return None
            except (OSError, FileNotFoundError) as error:
                print(f"File operation failed: {error}")
                return None
            except Exception as error:
                print(f"Unexpected error: {error}")
                return None

