#!/usr/bin/python3
def safe_print_integer(value):
    if value:
        try:
            attempted_int = int(value)
        except ValueError:
            return False
        print("{:d}".format(attempted_int))
        return True
