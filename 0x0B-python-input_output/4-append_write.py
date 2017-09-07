#!/usr/bin/python3
"""
This module can be used for append text
to a file
"""


def append_write(filename="", text=""):
    """
    Append text to a file

    Args:
        filename (str): The name of the file
        text (str): The text to append to the file
    """
    if type(filename) is not str:
        raise TypeError("filename needs to be a string")
    if type(text) is not str:
        raise TypeError("text needs to be a string")
    with open(filename, "a", encoding="utf-8") as text_file:
        chars = text_file.write(text)
    return chars
