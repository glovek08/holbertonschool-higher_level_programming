#!/usr/bin/python3
"""
"""
import math


def pascal_triangle(n):
    my_list = [1]
    i=0
    for el in my_list:
        if my_list[i] < n:
            my_list.append(n)
        print(my_list)


pascal_triangle(5)


