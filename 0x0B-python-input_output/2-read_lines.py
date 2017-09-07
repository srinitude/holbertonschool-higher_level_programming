#!/usr/bin/python3
"""
This module prints a certain number of lines
in a text file
"""


def read_lines(filename="", nb_lines=0):
    """
    Prints a certain number of lines in a file

    Args:
        filename (str): The name of the file
        nb_lines (int): The number of lines to print
    """
    if type(filename) is not str:
        raise TypeError("filename needs to be a string")
    if type(nb_lines) is not int:
        raise TypeError("nb_lines needs to be an integer")
    lines = []
    with open(filename, encoding="utf-8") as text_file:
        lines = text_file.readlines()
    total = len(lines)
    if nb_lines <= 0 or nb_lines >= total:
        for line in lines:
            print(line, end="")
    else:
        for i in range(nb_lines):
            print(lines[i], end="")
