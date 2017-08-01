#!/usr/bin/python3


def uppercase(str):
    strlen = len(str)
    if strlen == 0:
        print("{}".format(str))
        break
    for i, c in enumerate(str):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            upper = ord(c) - 32
            c = chr(upper)
        if i == (strlen - 1):
            print("{}".format(c))
        else:
            print("{}".format(c), end="")
