#!/usr/bin/python3
"""
BaseGeometry Module
"""


class BaseGeometry:
    """
    A class with very basic geometry functionality
    """
    def area(self):
        """
        Returns the area of the object that inherits this class
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates a particular integer
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """
    A Rectangle inherits from BaseGeometry
    """
    def __init__(self, width, height):
        """
        Initialization for a Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def __str__(self):
        """
        Pretty string representation of the object
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

    def area(self):
        """
        Returns the area of the Rectangle
        """
        return self.__width * self.__height


class Square(Rectangle):
    """
    A Square inherits from a Rectangle
    """
    def __init__(self, size):
        """
        Initialization for a Square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        Pretty string representation of the Square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

    def area(self):
        """
        Returns the area of the Square
        """
        return self.__size ** 2
