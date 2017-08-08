#!/usr/bin/python3


def valid_index(my_list, index):
    length = len(my_list)
    if index < 0 and abs(index) > length:
        return False
    elif index >= length:
        return False
    return True


def replace_in_list(my_list, idx, element):
    if valid_index(my_list, idx):
        del my_list[idx]
        my_list.insert(idx, element)
        return my_list
    return my_list
