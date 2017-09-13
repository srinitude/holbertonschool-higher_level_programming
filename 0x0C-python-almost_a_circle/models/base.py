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
            list_dictionaries = []
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """
        Decodes contents of a JSON string
        """
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save list objects to a file
        """
        if not list_objs:
            list_dicts = []
        else:
            list_dicts = list(map((lambda b: b.to_dictionary()), list_objs))
        json_str = Base.to_json_string(list_dicts)
        with open("{}.json".format(cls.__name__), "w") as json_file:
            json_file.write(json_str)

    @classmethod
    def create(cls, **dictionary):
        """
        Factory method to create a Base-subclassed object
        """
        if cls.__name__ == "Rectangle":
            obj = cls(1, 1)
        elif cls.__name__ == "Square":
            obj = cls(1)
        obj.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        """
        Loads Base subclass instances from a file
        """
        try:
            with open("{}.json".format(cls.__name__)) as json_file:
                ld = Base.from_json_string(json_file.read())
        except FileNotFoundError:
            return []
        instances = list(map((lambda d: cls.create(**d)), ld))
        return instances
