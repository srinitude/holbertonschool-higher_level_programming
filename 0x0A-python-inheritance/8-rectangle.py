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
