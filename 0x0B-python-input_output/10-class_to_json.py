#!/usr/bin/python3
"""
This module returns the serialized __dict__
of an object
"""


def class_to_json(obj):
    return obj.__dict__
