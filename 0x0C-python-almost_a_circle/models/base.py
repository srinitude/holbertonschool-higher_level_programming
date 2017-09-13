#!/usr/bin/python3
"""
This is the module for the Base class
"""


import json
import csv


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
    def to_csv_row(obj):
        """
        Create a row from a Base subclassed object
        """
        row = []
        if not obj:
            return
        row.append(str(obj.id))
        if type(obj).__name__ == "Rectangle":
            row.append(str(obj.width))
            row.append(str(obj.height))
        elif type(obj).__name__ == "Square":
            row.append(str(obj.size))
        row.append(str(obj.x))
        row.append(str(obj.y))
        return row

    @staticmethod
    def from_json_string(json_string):
        """
        Decodes contents of a JSON string
        """
        if not json_string or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def from_csv(cls, row):
        """
        Create a Base subclassed object from a CSV row
        """
        f = list(map((lambda arg: int(arg)), row))
        if cls.__name__ == "Rectangle":
            obj = cls(f[1], f[2], f[3], f[4], f[0])
        elif cls.__name__ == "Square":
            obj = cls(f[1], f[2], f[3], f[0])
        return obj

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
    def save_to_file_csv(cls, list_objs):
        """
        Saves list objects to CSV
        """
        if not list_objs:
            return
        with open("{}.csv".format(cls.__name__), 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file, delimiter=',')
            for obj in list_objs:
                row = Base.to_csv_row(obj)
                csv_writer.writerow(row)

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
        Loads Base subclass instances from a JSON file
        """
        try:
            with open("{}.json".format(cls.__name__)) as json_file:
                ld = Base.from_json_string(json_file.read())
        except FileNotFoundError:
            return []
        instances = list(map((lambda d: cls.create(**d)), ld))
        return instances

    @classmethod
    def load_from_file_csv(cls):
        """
        Loads Base subclass instances from a CSV file
        """
        with open("{}.csv".format(cls.__name__), newline='') as csv_file:
            reader = csv.reader(csv_file, delimiter=',')
            instances = list(map((lambda row: cls.from_csv(row)), reader))
            return instances
