#!/usr/bin/python3
"""
Is kind of class
"""
def is_kind_of_class(obj, a_class):
    """
    Checks to see if the object is same class
    or descendant
    """
    if isinstance(obj, a_class):
        return True
    return False
