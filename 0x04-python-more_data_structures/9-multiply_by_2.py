#!/usr/bin/python3


def multiply_by_2(my_dict):
    new_dict = my_dict.copy()
    for key in new_dict.keys():
        new_dict[key] *= 2
    return new_dict
