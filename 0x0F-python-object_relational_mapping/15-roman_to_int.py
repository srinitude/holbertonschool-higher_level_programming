#!/usr/bin/python3
"""
Roman Numeral To Integer program
"""


def roman_to_int(roman_string):
    """
    Roman Numeral To Integer program
    """
    if roman_string is None or type(roman_string) is not str:
        return 0
    letters = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    last = len(roman_string) - 1
    skip = False
    result = 0
    for i in range(last, -1, -1):
        if i == 0 and skip is False:
            result += letters[roman_string[i]]
            break
        if skip:
            skip = False
            continue
        p = i - 1
        if letters[roman_string[p]] < letters[roman_string[i]]:
            diff = letters[roman_string[i]] - letters[roman_string[p]]
            result += diff
            skip = True
        else:
            result += letters[roman_string[i]]
    return result
