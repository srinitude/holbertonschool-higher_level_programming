#!/usr/bin/python3

def uppercase(str):
    i, strlen = 0, len(str)
    for c in str:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            upper = ord(c) - 32
            c = chr(upper)
        if i == (strlen - 1):
            print(c)
        else:
            print(c, end="")
        i += 1
