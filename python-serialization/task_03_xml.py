#!/usr/bin/python3
"""
Module that uses XML serialization and deserialization
as an alternative format to JSON.
"""
import xml.etree.ElementTree as ET
from os import path
from typing import Optional


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
    obj_reconstructed_associative_array = collections.OrderedDict()
    try:
        obj_xml_tree_representation = ET.parse(filename)
        obj_xml_root_element = obj_xml_tree_representation.getroot()
        for obj_child_element in obj_xml_root_element:
            str_element_tag = obj_child_element.tag
            str_element_text_content = obj_child_element.text
            obj_reconstructed_associative_array[str_element_tag] = str_element_text_content
        return dict(obj_reconstructed_associative_array)
    except ET.ParseError as obj_parse_exception:
        print(f"[{__name__}] XML fucked up: {filename} {obj_parse_exception}")
        return None
    except Exception as obj_generic_exception:
        print(
            f"[{__name__}] Something else got fucked up: {filename} {obj_generic_exception}")
        return None
