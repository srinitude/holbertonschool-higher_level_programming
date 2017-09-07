#!/usr/bin/python3
"""
Module that serializes object into JSON
"""


from json import JSONEncoder


def to_json_string(my_obj):
    """
    Returns JSON representation of an object

    Args:
       my_obj (object): A Python object
    """
    if my_obj:
        return JSONEncoder().encode(my_obj)
    raise TypeError("Missing the object as an argument")
