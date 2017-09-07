#!/usr/bin/python3
def inherits_from(obj, a_class):
    if isinstance(obj, a_class) and type(obj) is not a_class:
        return True
    return False
