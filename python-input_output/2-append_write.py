#!/usr/bin/python3
"""
Module with function that append to text file
"""


def append_write(filename="", input_text=""):
    """
    Function that appends to a text file using UTF-8.
    Arguments:
        filename: path to file.
        input_text: the text to write.
    Return:
        Bytes written.
    """
    try:
        with open(filename, mode="a", encoding="utf-8") as a_file:
            bytes_written = a_file.write(input_text)
    except PermissionError as error:
        raise PermissionError
    except Exception as error:
        print(error)
    return bytes_written

# print(append_write("test123.txt", "I like her, but she doesn't like me.\n"))
