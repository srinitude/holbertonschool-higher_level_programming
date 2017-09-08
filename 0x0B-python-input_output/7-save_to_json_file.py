#!/usr/bin/python3
"""
This module is for writing Python objects to text
files.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Saves your Python object to the text file of your choice

    Args:
        my_obj (object): The object to serialize
        filename (str): The filename to add JSON to
    """
    if type(filename) is not str:
        raise TypeError("filename must be a string")
    with open(filename, "w", encoding="utf-8") as text_file:
        json.dump(my_obj, text_file)
