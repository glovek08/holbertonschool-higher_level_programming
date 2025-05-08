#!/usr/bin/python3

def print_last_digit(num):
    if (num < 0):
        res = ((num * -1) % 10) * -1
    else:
        res = num % 10
    print(res, end="")
    return (res)
