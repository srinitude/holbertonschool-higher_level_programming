#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    printed = 0
    for i in range(x):
        try:
            attempted_int = int(my_list[i])
        except (ValueError, TypeError):
            continue
        else:
            print("{:d}".format(attempted_int), end="")
            printed += 1
    print("")
    return printed
