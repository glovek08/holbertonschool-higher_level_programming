#!/usr/bin/python3
num = 0
while num <= 98:
    def get_hex(n):
        temp = str(n)
        result = "".join([c for c in hex(n)])
        return result
    joint_str = "".join(chr(ord(c)) for c in " = ")
    print("{decimal}{joint_str}{hexa}".format(
        decimal=int(str(num)),
        joint_str=joint_str,
        hexa="".join([char for char in get_hex(num)])
    ))
    num += int("1")
