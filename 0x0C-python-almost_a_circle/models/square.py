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
        super().__init__(size, size, x, y)

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
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """
        Update the values of the Square attributes
        """
        args_props = {
            "id": 0,
            "_Rectangle__width": 1,
            "_Rectangle__height": 1,
            "_Rectangle__x": 2,
            "_Rectangle__y": 3
        }
        length = len(args)
        for i in range(length):
            for key, val in args_props.items():
                if i == val:
                    self.__dict__[key] = args[i]
        kargs_props = {
            "id": "id",
            "_Rectangle__width": "size",
            "_Rectangle__height": "size",
            "_Rectangle__x": "x",
            "_Rectangle__y": "y"
        }
        for kw_key, kw_val in kwargs.items():
            for key, val in kargs_props.items():
                if kw_key == val:
                    self.__dict__[key] = kw_val
