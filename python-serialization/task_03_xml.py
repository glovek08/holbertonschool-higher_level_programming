#!/usr/bin/python3
"""
Module that uses XML serialization and deserialization
as an alternative format to JSON.
"""
import xml.etree.ElementTree as ET
from os import path
from typing import Optional
import collections


def serialize_to_xml(dictionary, filename):
    if isinstance(dictionary, dict)\
            and isinstance(filename, str):
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
        except Exception as error:
            print(f"Error writing XML to file: {error}")
    else:
        print("Invalid input: 'dictionary' must be a dict\
            and 'filename' must be a string.")


def deserialize_from_xml(filename: str) -> Optional[dict]:
    if not isinstance(filename, str):
        print(f"{__name__}")
        return None
    if not path.exists(filename):
        print(f"[{__name__}] CRITICAL ERROR: '{filename}")
        return None
    obj_array = collections.OrderedDict()
    try:
        obj_tree = ET.parse(filename)
        obj_root = obj_tree.getroot()
        for obj_child_element in obj_root:
            str_element_tag = obj_child_element.tag
            str_element_text_content = obj_child_element.text
            obj_array[str_element_tag] = str_element_text_content
        return dict(obj_array)
    except ET.ParseError as obj_parse_error:
        print(f"[{__name__}] XML fucked up: {filename} {obj_parse_error}")
        return None
    except Exception as error:
        print(
            f"[{__name__}] Something else got fucked up: {filename} {error}")
        return None
