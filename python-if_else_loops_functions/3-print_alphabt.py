#!/usr/bin/python3
char = 97
while char < 123:
    if char == 113 or char == 101:
        char += 1
    print("{}".format(chr(char)), end="")
    char += 1
