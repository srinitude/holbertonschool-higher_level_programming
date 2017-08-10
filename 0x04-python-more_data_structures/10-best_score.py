#!/usr/bin/python3


def best_score(my_dict):
    if not my_dict:
        return None
    keys = list(my_dict.keys())
    biggest_key = keys[0]
    biggest_value = my_dict.get(biggest_key)
    for key in keys[1:]:
        if my_dict.get(key) > biggest_value:
            biggest_key = key
            biggest_value = my_dict.get(biggest_key)
    return biggest_key
