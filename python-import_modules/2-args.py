#!/usr/bin/python3
from sys import argv

argc = len(argv) - 1
if (argc == 0):
    print("0 arguments.")
    exit()
elif (argc == 1):
    print("1 argument:")
else:
    print(f"{argc} arguments:")
    argv.pop(0)
for arg in argv:
    print(f"{argv.index(arg) + 1}: {arg}")
