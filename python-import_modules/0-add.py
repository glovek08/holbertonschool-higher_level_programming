#!/usr/bin/python3
from add_0 import add

if __name__ == "__main__":
    a = 1; b = 2
    print("{a} + {b} = {add_fun}".format(a=a, b=b, add_fun=add(a,b)))


