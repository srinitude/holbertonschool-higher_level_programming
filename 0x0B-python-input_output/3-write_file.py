#!/usr/bin/python3
"""
This module can be used for writing text
to a file
"""


def write_file(filename="", text=""):
    """
    Write text to a file

    Args:
        filename (str): The name of the file
        text (str): The text to write to the file
    """
    if type(filename) is not str:
        raise TypeError("filename needs to be a string")
    if type(text) is not str:
        raise TypeError("text needs to be a string")
    with open(filename, "w", encoding="utf-8") as text_file:
        chars = text_file.write(text)
    return chars
