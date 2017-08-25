#!/usr/bin/python
def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    special_chars = ['.', '?', ':']
    skip = None
    for char in text:
        if skip:
            print("\n")
            skip = None
        else:
            print(char, end="")
        if char in special_chars:
            skip = 1
