#!/usr/bin/python3
"""
Module with function that writes to text file
"""


def write_file(filename="", input_text=""):
    """
    Function that writes to a file using UTF-8.
    Arguments:
        filename: path to file.
        input_text: the text to write.
    """
    with open(filename, mode="w", encoding="utf-8") as a_file:
        try:
            # print(a_file.writable())
            characters_written = a_file.write(input_text)
        except Exception as error:
            print(error)
            return 0
        return characters_written

# write_file("test123.txt", "Holberton School is so cool!\n")
