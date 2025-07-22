#!/usr/bin/python3
def magic_string():
    magic_string.my_str = getattr(magic_string, "my_str", [])
    magic_string.my_str.append("BestSchool")
    return ", ".join(magic_string.my_str) + "$"
