#!/usr/bin/python3
def uppercase(str):
    str_to_byte = []
    for char in str:
        char = ord(char)
        if (char >= 65 and char <= 122):
            if (char >= 97 and char <= 122):
                char -= 32
            str_to_byte.append(chr(char))
    print("{str}".format(str = (''.join(str_to_byte))))

