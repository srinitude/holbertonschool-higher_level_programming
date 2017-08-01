#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)


def last_digit(number):
    ld = number % 10
    if number < 0:
        number = abs(number)
        ld = -(number % 10)
        return ld
    return ld

ld = last_digit(number)
if ld > 5:
    print("Last digit of", number, "is", ld, "and is greater than 5")
elif ld == 0:
    print("Last digit of", number, "is", ld, "and is 0")
elif ld < 6 and ld != 0:
    print("Last digit of", number, "is", ld, "and is less than 6 and not 0")
