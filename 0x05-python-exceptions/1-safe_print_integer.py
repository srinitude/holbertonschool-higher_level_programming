#!/usr/bin/python3
def safe_print_integer(value):
    if not value:
        return False
    try:
        attempted_int = int(value)
    except (ValueError, TypeError):
        return False
    print("{:d}".format(attempted_int))
    return True
