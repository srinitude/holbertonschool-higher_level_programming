#!/usr/bin/python3


def max_integer(my_list=[]):
    length = len(my_list)
    if length is 0:
        return None
    biggest = my_list[0]
    for i in range(1, length):
        if my_list[i] > biggest:
            biggest = my_list[i]
    return biggest
