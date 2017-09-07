#!/usr/bin/python3
"""
Inherits from
"""
def inherits_from(obj, a_class):
    """
    Determines if the obj is a descendant, not of the same type
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
