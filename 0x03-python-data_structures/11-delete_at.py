#!/usr/bin/python3


def valid_index(my_list, index):
    length = len(my_list)
    if length is 0:
        return False
    elif index < 0:
        return False
    elif index >= length:
        return False
    return True


def delete_at(my_list=[], idx=0):
    if valid_index(my_list, idx):
        del my_list[idx]
        return my_list
    return my_list
