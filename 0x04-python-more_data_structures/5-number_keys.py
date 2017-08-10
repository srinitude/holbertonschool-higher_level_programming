#!/usr/bin/python3


def number_keys(my_dict):
    if not my_dict:
        return 0
    keys = my_dict.keys()
    return len(keys)
