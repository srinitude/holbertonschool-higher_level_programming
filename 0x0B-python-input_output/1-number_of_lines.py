#!/usr/bin/python3
"""
This module allows you to count the number of lines
in a text file
"""


def number_of_lines(filename=""):
    """
    Returns the number of lines in a text file

    Args:
        filename (str): The name of the file
    """
    num_lines = 0
    with open(filename, encoding="utf-8") as text_file:
        for line in text_file:
            num_lines += 1
    return num_lines
