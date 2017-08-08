#!/usr/bin/python3


def element_at(my_list, idx):
    length = len(my_list)
    if length is 0:
        return None
    elif idx < 0:
        return None
    elif idx >= length:
        return None
    return my_list[idx]
