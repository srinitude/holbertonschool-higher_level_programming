#!/usr/bin/python3


def no_c(my_string):
    chars = [c for c in my_string if c != 'c' and c != 'C']
    new_string = "".join(chars)
    return new_string
