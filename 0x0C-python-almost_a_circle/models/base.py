#!/usr/bin/python3
"""
This is the module for the Base class
"""


import json


class Base:
    """
    The Base class consists of basic functionality

    Attributes:
        __nb_objects (int): The number of objects
        id (int): The id of the object
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initialization of the Base class

        Args:
            id (int): The id of the Base object
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        JSON representation of a list of dictionaries
        """
        if not list_dictionaries or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)
