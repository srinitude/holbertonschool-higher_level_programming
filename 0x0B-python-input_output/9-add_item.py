#!/usr/bin/python3
"""
This script will allow you to dynamically save items
to a persistent Python list object
"""


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    empty_list = []
    try:
        list_obj = load_from_json_file("add_item.json")
    except FileNotFoundError:
        save_to_json_file(empty_list, "add_item.json")
        list_obj = empty_list
    argc = len(argv)
    if argc > 1:
        for i in range(1, argc):
            list_obj.append(argv[i])
    save_to_json_file(list_obj, "add_item.json")
