#!/usr/bin/python3
"""
Module that parses JSON into Python object
"""


from json import JSONDecoder


def from_json_string(my_str):
    """
    Returns parsed Python object

    Args:
       my_str (str): A JSON string
    """
    if my_str is None:
        raise TypeError("Missing JSON as an argument")
    if type(my_str) is not str:
        raise TypeError("my_str needs to be JSON (i.e. a string)")
    return JSONDecoder().decode(my_str)
