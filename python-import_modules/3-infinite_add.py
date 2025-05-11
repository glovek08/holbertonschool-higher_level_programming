#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    result = []
    argv = argv[1:]
    for arg in argv:
        try:
            value = int(arg)
            result.append(value)
        except ValueError:
            continue
    print(sum(result))
