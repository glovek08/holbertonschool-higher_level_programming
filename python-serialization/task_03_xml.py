#!/usr/bin/python3
"""
Module that uses XML serialization and deserialization
as an alternative format to JSON.
"""
import xml.etree.ElementTree as ET
from os import path


def serialize_to_xml(dictionary, filename):
    if isinstance(dictionary, dict)\
            and isinstance(filename, str)\
            and path.exists(filename):
        # with open(filename, 'r', encoding='utf-8') as file:
        #     content = file.read()
        #     print(content)
        # tree = ET.parse(tree)
        root = ET.Element("data")
        for key, value in dictionary.items():
            child_el = ET.SubElement(root, str(key))
            child_el.text = str(value)
        tree = ET.ElementTree(root)
        try:
            ET.indent(tree, space="  ", level=0)
            tree.write(filename, encoding="utf-8")
        except Exception as e:
            print(f"Error writing XML to file: {e}")
    else:
        print("Invalid input: 'dictionary' must be a dict\
            and 'filename' must be a string.")


def deserialize_from_xml(filename):
    pass
