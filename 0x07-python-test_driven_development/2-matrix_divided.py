#!/usr/bin/python3

def check_for_ints_and_floats(matrix):
    bad_input = "matrix must be a matrix (list of lists) of integers/floats"
    flat_list = [i for sublist in matrix for i in sublist]
    for i in flat_list:
        if type(i) is not int and type(i) is not float:
            raise TypeError(bad_input)

def make_sure_lists_are_same_length(matrix):
    needed_length = len(matrix[0])
    for i, sublist in enumerate(matrix):
        if i == 0:
            continue
        list_length = len(sublist)
        if list_length != needed_length:
            raise TypeError("Each row of the matrix must have the same size")

def check_for_div_type(div):
    if type(div) is not int and type(div) is not float:
        raise TypeError("div must be a number")

def check_for_zero_division(div):
    if div == 0:
        raise ZeroDivisionError("division by zero")

def number_of_lists(matrix):
    count = 0
    for sublist in matrix:
        count += 1
    return count

def matrix_divided(matrix, div):
    check_for_ints_and_floats(matrix)
    count = number_of_lists(matrix)
    if count == 0:
        return []
    make_sure_lists_are_same_length(matrix)
    check_for_div_type(div)
    check_for_zero_division(div)
    new_matrix = []
    for sublist in matrix:
        new_list = list(map((lambda x: round(x / div, 2)), sublist))
        new_matrix.append(new_list)
    return new_matrix

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
