#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    for key in a_dictionary:
        if isinstance(a_dictionary[key], int):
            try:
                a_dictionary[key] *= 2
            except Exception as error:
                print(error)
                continue
    return a_dictionary
