#!/usr/bin/python3
"""
Module that saves structured data with json to text file
"""
import json


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object (string).
    Args:
        my_obj: The object to serialize to JSON.
    Returns:
        str: The JSON string representation of the object.
    """
    try:
        return json.dumps(my_obj)
    except Exception as error:
        print(error)