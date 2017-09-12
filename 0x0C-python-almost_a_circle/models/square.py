#!/usr/bin/python3
"""
This module is all about Squares
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    A Square inherits from a Rectangle

    Attributes:
        size (int): The length of a Square's side
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Initialization of a Square
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """
        The pretty string representation of a Square
        """
        rep = "[Square] ({:d}) {:d}/{:d} - {:d}"
        return rep.format(self.id, self.x, self.y, self.height)

    @property
    def size(self):
        """
        Getter for Square's size attribute
        """
        return self.width

    @size.setter
    def size(self, value):
        """
        Setter for Square's size attribute
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the values of the Square attributes
        """
        length = len(args)
        if length:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.size = arg
                if i == 2:
                    self.x = arg
                if i == 3:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "size" in kwargs:
                self.size = kwargs.get("size")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """
        Dictionary representation of a square
        """
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["size"] = self.width
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict
