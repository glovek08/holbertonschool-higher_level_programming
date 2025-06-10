#!/usr/bin/python3
"""
"""
import math


def pascal_triangle(n):
    my_list = []
    last_index = 0
    next_index = 0
    for num in range(n): # Generate a fixed-length list.
        my_list.append(last_index)
    for el in my_list:
        pass
    print(my_list)




pascal_triangle(5)

# [1]
# [1,1]
# [1,2,1]
# [1,3,3,1]
# [1,4,6,4,1]
