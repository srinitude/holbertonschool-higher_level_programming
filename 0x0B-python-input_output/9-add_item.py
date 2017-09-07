#!/usr/bin/python3
"""
This script will allow you to dynamically save items
to a persistent Python list object
"""


from sys import argv
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file

if __name__ == "__main__":
    try:
        list_obj = load_from_json_file("add_item.json")
    except FileNotFoundError:
        list_obj = []
    argc = len(argv)
    if argc > 1:
        for i in range(1, argc):
            list_obj.append(argv[i])
    save_to_json_file(list_obj, "add_item.json")
