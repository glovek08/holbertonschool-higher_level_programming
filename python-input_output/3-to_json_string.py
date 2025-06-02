#!/usr/bin/python3
"""
Module that saves structured data with json to text file
"""
import json


def to_json_string(my_obj):
    try:
        return json.dumps(my_obj)
    except Exception as error:
        print(error)