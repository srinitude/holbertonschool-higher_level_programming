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

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/7-base_geometry.txt")
