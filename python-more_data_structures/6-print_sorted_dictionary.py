#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    a_dcty_temp = a_dictionary.copy()
    for key, val in sorted(a_dcty_temp.items()):
        print(f"{key}: {val}")
