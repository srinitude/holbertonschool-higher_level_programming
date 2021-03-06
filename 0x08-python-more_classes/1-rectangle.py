#!/usr/bin/python3
"""
Here's an implementation of a Rectangle
"""


class Rectangle:
    """
    Args:
        width (int): The width of the Rectangle
        height (int): The height of the Rectangle
    """
    def __init__(self, width=0, height=0):
        """
        Initialization of a Rectangle after it gets instantiated

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Getter for private width Rectangle attribute

        Returns:
            Width of the Rectangle
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter for private width Rectangle attribute

        Args:
           value (int): The width of the Rectangle
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter for private height Rectangle attribute

        Returns:
            Height of the Rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Setter for private height Rectangle attribute

        Args:
           value (int): The height of the Rectangle
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
