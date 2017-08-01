#!/usr/bin/python3


def ones_place(n):
    ld = n % 10
    if n < 0:
        n = abs(n)
        ld = n % 10
    return ld


def print_last_digit(number):
    last_digit = ones_place(number)
    print(last_digit, end="")
    return last_digit
