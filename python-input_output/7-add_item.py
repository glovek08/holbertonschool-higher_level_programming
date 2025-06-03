#!/usr/bin/python3
"""
Module that adds specified
arguments to a file using JSON and then loads them.
"""
import json
from sys import argv
JSON_save = __import__("5-save_to_json_file").save_to_json_file
JSON_load = __import__("6-load_from_json_file").load_from_json_file

filename = 'add_item.json'

# print(argv)
my_list = argv[1:]
# print(my_list)

try:
    list_exists = JSON_load(filename)
except FileNotFoundError:
    list_exists = []
except json.JSONDecodeError:
    # File not JSON
    list_exists = []

list_exists.extend(my_list)

JSON_save(list_exists, filename)
JSON_load(filename)
