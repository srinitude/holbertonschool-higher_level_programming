#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/1-my_list.txt")
