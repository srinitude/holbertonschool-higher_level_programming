#!/usr/bin/python3


def simple_delete(my_dict, key=""):
    if isinstance(key, str):
        if my_dict.get(key):
            del my_dict[key]
    return my_dict
