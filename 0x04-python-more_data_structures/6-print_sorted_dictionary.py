#!/usr/bin/python3


def print_sorted_dictionary(my_dict):
    if not my_dict:
        return
    sorted_keys = sorted(my_dict.keys())
    for key in sorted_keys:
        print("{:s}: {}".format(key, my_dict.get(key)))
