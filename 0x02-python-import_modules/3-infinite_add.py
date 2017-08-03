#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    sum = 0
    for i, arg in enumerate(argv):
        if i != 0:
            num = int(arg)
            sum += num
    print(sum)
