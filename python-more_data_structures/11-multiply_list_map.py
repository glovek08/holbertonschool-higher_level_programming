#!/usr/bin/python3

# list1 = [2, 10, 12, 21]

def multiply_list_map(my_list=[], number=0):
    new_list = map(lambda el: el * number, my_list)
    return list(new_list)

# print(multiply_list_map(list1, 2))
# print(list1)
