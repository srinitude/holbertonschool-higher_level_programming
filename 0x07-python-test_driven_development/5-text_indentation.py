#!/usr/bin/python
"""Text indentation module"""

def text_indentation(text):
    """Text indentation function"""
    if type(text) is not str:
        raise TypeError("text must be a string")
    special_chars = ['.', '?', ':']
    length = len(text)
    skip = None
    for i, char in enumerate(text, 1):
        if skip:
            print("\n")
            skip = None
        else:
            print(char, end="")
        if char in special_chars:
            skip = 1
        if i == length:
            last_char = char

    if last_char in special_chars:
        print("\n")

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/5-text_indentation.txt")
