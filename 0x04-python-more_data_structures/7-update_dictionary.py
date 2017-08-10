#!/usr/bin/python3


def update_dictionary(my_dict, key, value):
    if not my_dict:
        return
    my_dict[key] = value
    return my_dict
