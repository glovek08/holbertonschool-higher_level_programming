#!/usr/bin/python3
"""
Module with function to handle JSON shit
"""
import json


def from_json_string(my_str):
    """
    Takes a string and produces its object repr (Python data structure)
    represented by a JSON string.
    Args:
        my_str: The JSON string to get its representation in python style.
    Returns:
        str: The object repr in python style from a JSON string.
    """
    try:
        return json.loads(my_str)
    except json.JSONDecodeError as json_error:
        raise json_error
    except Exception as error:
        raise Exception
