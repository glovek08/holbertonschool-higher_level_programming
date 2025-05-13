#!/usr/bin/python3

def max_integer(my_list=[]):
    list_len = len(my_list)
    if (list_len == 0):
        return None
    
    max_value = 0
    print(my_list, list_len)
    for each in my_list:
        if each > max_value:
            max_value = each
    print(max_value)
