#!/usr/bin/python3


def tuple_check(tup):
    length = len(tup)
    if length == 0:
        new_tup = (0, 0)
        del tup
        return new_tup
    elif length == 1:
        new_tup = (tup[0], 0)
        del tup
        return new_tup
    return tup


def add_tuple(tuple_a=(), tuple_b=()):
    sum_list = []
    tuple_a = tuple_check(tuple_a)
    tuple_b = tuple_check(tuple_b)
    zip_tuples = zip(tuple_a, tuple_b)
    for i, tup in enumerate(zip_tuples):
        if i < 2:
            first, second = tup
            sum_list.append(first + second)
    return tuple(sum_list)
