#!/usr/bin/python3

for i in range(100):
    if i != 99:
        print("{0:02d}".format(i), end=", ")
        continue
    print(99)
