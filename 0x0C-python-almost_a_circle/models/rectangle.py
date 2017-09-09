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
        super.__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

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
        self.__y = value
