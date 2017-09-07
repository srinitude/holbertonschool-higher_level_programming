#!/usr/bin/python3
"""
Is same class?
"""


def is_same_class(obj, a_class):
    """
    Checks to see if the obj is of the same class
    """
    if type(obj) is a_class:
        return True
    return False
