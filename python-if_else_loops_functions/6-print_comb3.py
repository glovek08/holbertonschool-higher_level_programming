#!/usr/bin/python3
for num in range(100):
    if (str(num) != str(num)[::-1]):
        print("{num:02}".format(num = num), end=", ")
