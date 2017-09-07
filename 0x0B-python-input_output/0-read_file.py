#!/usr/bin/python3
"""
This module contains information about reading
a UTF-8 encoded text file
"""


def read_file(filename=""):
    """
    Prints a UTF-8 file line by line

    Args:
        filename (str): The name of the file
    """
    if type(filename) is not str:
        raise TypeError("filename must be a string")
    with open(filename, encoding="utf-8") as text_file:
        for line in text_file:
            print(line, end="")
