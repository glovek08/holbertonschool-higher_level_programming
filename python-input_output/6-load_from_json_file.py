#!/usr/bin/python3
"""
This module has a function for creating object from JSON files.
"""
import json


def load_from_json_file(filename):
    with open(filename, mode="r", encoding="utf-8") as a_file:
        try:
            new_obj = json.load(filename)
        except Exception as error:
            raise error
    return new_obj
