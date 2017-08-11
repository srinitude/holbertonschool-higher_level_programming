#!/usr/bin/python3


def complex_delete(my_dict, value):
    for key in list(my_dict.keys()):
        if my_dict[key] == value:
            del my_dict[key]
    return my_dict
