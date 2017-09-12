#!/usr/bin/python3
"""
This is the module for the Rectangle class
"""


from models.base import Base


class Rectangle(Base):
    """
    Blueprint for a Rectangle

    Attributes:
        width (int): The width of the Rectangle
        height (int): The height of the Rectangle
        x (int): The x coordinate of the Rectangle
        y (int): The y coordinate of the Rectangle
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        The initialization of the Rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """
        The pretty representation of a Rectangle
        """
        rep = "[Rectangle] ({:d}) {:d}/{:d} - {:d}/{:d}"
        return rep.format(self.id, self.x, self.y, self.width, self.height)

    @property
    def width(self):
        """
        Getter for the Rectangle width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for the Rectangle width
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for the Rectangle height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for the Rectangle height
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """
        Getter for the Rectangle x coord
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
        Setter for the Rectangle x coord
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """
        Getter for the Rectangle y coord
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
        Setter for the Rectangle y coord
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >=0")
        self.__y = value

    def area(self):
        """
        Returns the area of the Rectangle
        """
        return self.__width * self.__height

    def display(self):
        """
        Prints the Rectangle to stdout
        """
        rect = ""
        for i in range(self.__y):
            rect += "\n"
        for i in range(self.__height):
            row_offset = " " * self.__x
            rect += row_offset
            for j in range(self.__width):
                rect += "#"
            rect += "\n"
        print(rect[:-1])

    def update(self, *args, **kwargs):
        """
        Update the values of the Rectangle attributes
        """
        length = len(args)
        if length:
            for i, arg in enumerate(args):
                if i == 0:
                    self.id = arg
                if i == 1:
                    self.width = arg
                if i == 2:
                    self.height = arg
                if i == 3:
                    self.x = arg
                if i == 4:
                    self.y = arg
        else:
            if "id" in kwargs:
                self.id = kwargs.get("id")
            if "width" in kwargs:
                self.width = kwargs.get("width")
            if "height" in kwargs:
                self.height = kwargs.get("height")
            if "x" in kwargs:
                self.x = kwargs.get("x")
            if "y" in kwargs:
                self.y = kwargs.get("y")

    def to_dictionary(self):
        """
        Dictionary reppresentation of a Rectangle
        """
        new_dict = {}
        new_dict["id"] = self.id
        new_dict["width"] = self.width
        new_dict["height"] = self.height
        new_dict["x"] = self.x
        new_dict["y"] = self.y
        return new_dict
