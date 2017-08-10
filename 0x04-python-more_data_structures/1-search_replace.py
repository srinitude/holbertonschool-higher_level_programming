#!/usr/bin/python3


def search_replace(my_list, search, replace):
    if isinstance(my_list, list):
        if not search:
            return my_list
        if not replace:
            return my_list
        new_list = []
        for i in my_list:
            if i == search:
                new_list.append(replace)
            else:
                new_list.append(i)
        return new_list
