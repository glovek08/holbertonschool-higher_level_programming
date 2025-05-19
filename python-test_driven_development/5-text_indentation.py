#!/usr/bin/python3
"""
    This module is well documented.
"""


def text_indentation(text):
    """
        prints a text with 2 new lines after
        each of these characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    tx1 = text.replace('.', '.\n\n').replace(
        '?', '?\n\n').replace(':', ':\n\n')
    tx = tx1.strip(" ")
    print("{:s}".format(tx))
