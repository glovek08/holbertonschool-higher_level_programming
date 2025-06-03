#!/usr/bin/python3
"""
"""
import json

def from_json_string(my_str):
    try:
        return json.loads(my_str)
    except TypeError:
        raise TypeError("Object of type set is not JSON serializable")
    except Exception as error:
        raise Exception