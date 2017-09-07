#!/usr/bin/python3
"""
This module returns the serialized __dict__
of an object
"""


from json import JSONEncoder


def class_to_json(obj):
    return JSONEncoder().encode(obj.__dict__)
