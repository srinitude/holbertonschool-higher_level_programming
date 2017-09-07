#!/usr/bin/python3
"""
This module is for writing Python objects to text
files.
"""


from json import JSONEncoder


def save_to_json_file(my_obj, filename):
    """
    Saves your Python object to the text file of your choice

    Args:
        my_obj (object): The object to serialize
        filename (str): The filename to add JSON to
    """
    if type(filename) is not str:
        raise TypeError("filename must be a string")
    obj_str = JSONEncoder().encode(my_obj)
    with open(filename, "w", encoding="utf-8") as text_file:
        text_file.write(obj_str)
