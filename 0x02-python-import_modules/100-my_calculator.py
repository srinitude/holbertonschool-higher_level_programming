#!/usr/bin/python3
from sys import argv, exit
from calculator_1 import add, sub, mul, div


def find_handler(op):
    allowed_ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div
    }
    if allowed_ops.get(op):
        return allowed_ops[op]
    print("Unknown operator. Available operators: +, -, * and /")
    exit(1)

if __name__ == "__main__":
    def convert_to_int(str):
        try:
            i = int(str)
            return i
        except ValueError:
            print("Pass in actual integers")
            exit(1)

    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    left = convert_to_int(argv[1])
    right = convert_to_int(argv[3])
    op = argv[2]
    handler = find_handler(op)
    print(left, op, right, "=", handler(left, right))
