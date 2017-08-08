#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for arr in matrix:
        length = len(arr)
        if length == 0:
            print("")
            continue
        last_index = length - 1
        for i, n in enumerate(arr):
            if i < last_index:
                print("{:d}".format(n), end=" ")
                continue
            print("{:d}".format(n))
