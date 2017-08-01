#!/usr/bin/python3


def uppercase(str):
    for c in (str):
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            upper = ord(c) - 32
            c = chr(upper)
        print("{}".format(c), end="")
    print("")
