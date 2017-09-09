#!/usr/bin/python3
"""
This is the module for the Base class
"""


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
            self.id = self.__nb_objects
