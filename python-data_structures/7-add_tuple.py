#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    #tuple_a
    a_len = len(tuple_a)
    if (a_len == 0):
        tuple_a = (0, 0)
    elif (a_len == 1):
        tuple_a = (tuple_a[0], 0)
    else:
        tuple_a = (tuple_a[0], tuple_a[1])

    #tuple_b
    b_len = len(tuple_b)
    if (b_len == 0):
        tuple_b = (0, 0)
    elif (b_len == 1):
        tuple_b = (tuple_b[0], 0)
    else:
        tuple_b = (tuple_b[0], tuple_b[1])

    new_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    return new_tuple
