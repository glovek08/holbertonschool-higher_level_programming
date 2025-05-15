#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dict = a_dictionary.copy()
    for key in new_dict:
        if isinstance(new_dict[key], int):
            try:
                new_dict[key] *= 2
            except Exception as error:
                print(error)
                continue
    return new_dict
