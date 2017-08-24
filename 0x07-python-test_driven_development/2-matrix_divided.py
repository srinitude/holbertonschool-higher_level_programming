#!/usr/bin/python3
def matrix_divided(matrix, div):
    bad_input = "matrix must be a matrix (list of lists) of integers/floats"
    flat_list = [i for sublist in matrix for i in sublist]
    for i in flat_list:
        if type(i) is not int and type(i) is not float:
            raise TypeError(bad_input)
    needed_length = len(matrix[0])
    for i, sublist in enumerate(matrix):
        if i == 0:
            continue
        list_length = len(sublist)
        if list_length != needed_length:
            raise TypeError("Each row of the matrix must have the same size")
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for sublist in matrix:
        new_list = list(map((lambda x: round(x / div, 2)), sublist))
        new_matrix.append(new_list)
    return new_matrix
