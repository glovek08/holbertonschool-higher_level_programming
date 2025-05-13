#!/usr/bin/python3

def multiple_returns(strg):
    strg_len = len(strg)
    if not strg_len:
        new_tuple = (0, None)
    else:
        new_tuple = tuple((strg_len, strg[0]))
    return (new_tuple)
