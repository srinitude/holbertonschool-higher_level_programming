#!/usr/bin/python3
def safe_print_integer(value):
    try:
        attempted_int = int(value)
    except (ValueError, TypeError):
        return False
    else:
        print("{:d}".format(attempted_int))
        return True
