#!/usr/bin/python3


def valid_index(my_list, index):
    length = len(my_list)
    if (index < 0) and (abs(index) > length):
        return False
    elif index >= length:
        return False
    return True


def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    if valid_index(new_list, idx):
        del new_list[idx]
        new_list.insert(idx, element)
        return new_list
    del new_list
    return my_list
