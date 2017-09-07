#!/usr/bin/python3
"""
New list subclass MyList
"""


class MyList(list):
    """
    Nothing much more to MyList
    """
    def print_sorted(self):
        """
        Prints the current instance in sorted order
        """
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
