#!/usr/bin/python3
def safe_print_integer_err(value):
    from sys import stderr
    try:
        print("{:d}".format(value))
    except ValueError as ve:
        print("Exception: {}".format(ve), file=stderr)
        return False
    except TypeError as te:
        print("Exception: {}".format(ve), file=stderr)
        return False
    else:
        return True
