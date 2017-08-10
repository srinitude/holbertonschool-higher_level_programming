#!/usr/bin/python3


def square_matrix_simple(matrix=[]):
    if not matrix:
        return
    new_matrix = []
    for row in matrix:
        new_row = list(map((lambda x: x ** 2), row))
        new_matrix.append(new_row)
    return new_matrix
