#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new_list = []
    for each in my_list:
        new_list.append(replace) if each == search else new_list.append(each)
    return new_list
