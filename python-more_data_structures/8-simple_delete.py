#!/usr/bin/python3

def simple_delete(a_dictionary, key=""):
    try:
        a_dictionary.pop(key)
    except Exception as error:
        print("Couldn't delete item: ", end='')
        print(error)
        return -1
    return a_dictionary
