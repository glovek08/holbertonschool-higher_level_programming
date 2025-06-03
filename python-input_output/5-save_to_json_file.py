#!/usr/bin/python3
"""
Module with function to handle JSON shit
"""
import json


def save_to_json_file(my_obj, filename):
    """Saves a Python object to a JSON file.
    Args:
        my_obj: The object to save.
        filename (str): The file path.
    """
    try:
        with open(filename, mode='w', encoding="utf-8") as a_file:
            json.dump(my_obj, a_file)
    except Exception as error:
        print(error)
