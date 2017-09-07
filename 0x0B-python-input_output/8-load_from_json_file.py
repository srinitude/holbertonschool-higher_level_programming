#!/usr/bin/python3
"""
This module loads a Python object from a JSON file
"""


from json import JSONDecoder


def load_from_json_file(filename):
    """
    Returns object from JSON file

    Args:
        filename (str): The name of the file
    """
    if type(filename) is not str:
        raise TypeError("filename must be a string")
    with open(filename, encoding="utf-8") as json_file:
        obj_str = json_file.read()
    return JSONDecoder().decode(obj_str)
