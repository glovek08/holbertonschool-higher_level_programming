#!/usr/bin/python3
"""
    This module documentation is excellent.
"""
def max_integer(list=[]):
    """
        This function documentation is excellent.
        Bro just ask copilot.
    """
    if list == []:
        return None
    my_list = list.copy()
    for i in range(0, len(my_list)):
        for j in range(0, len(my_list) - 1):
            if my_list[j] > my_list[j + 1]:
                temp = my_list[j]
                my_list[j] = my_list[j + 1]
                my_list[j + 1] = temp
    biggest = my_list[len(my_list) - 1]
    return biggest
