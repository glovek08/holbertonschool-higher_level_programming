#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    argc = len(argv) - 1
    if (argc == 0):
        print("0 arguments.")
        exit()
    argv.pop(0)
    if (argc == 1):
        print("1 argument:")
    else:
        print(f"{argc} arguments:")
    for arg in argv:
        print(f"{argv.index(arg) + 1}: {arg}")
