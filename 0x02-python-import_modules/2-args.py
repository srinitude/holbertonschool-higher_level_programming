#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num = len(argv) - 1
    punc = ":"
    plural = "s"

    if num == 0:
        punc = "."
    if num <= 1:
        plural = ""

    print("{:d} argument{:s}{:s}".format(num, plural, punc))

    for i, arg in enumerate(argv):
        if i != 0:
            print("{:d}: {:s}".format(i, arg))
