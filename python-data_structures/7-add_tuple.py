#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    #tuple_a
    if (len(tuple_a) != 2):
        a_len = len(tuple_a)
        if (a_len == 0):
            tuple_a = (0, 0)
        elif (a_len < 2):
            tuple_a = (tuple_a[0], 0)
    #tuple_b
    elif (len(tuple_b) != 2):
        b_len = len(tuple_b)
        if (b_len == 0):
            tuple_b = (0, 0)
        elif (b_len < 2):
            tuple_b = (tuple_b[0], 0)
        
    new_tuple = ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
    return new_tuple
