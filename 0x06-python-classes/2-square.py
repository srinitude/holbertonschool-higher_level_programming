#!/usr/bin/python3
"""
This module contains documentation for a Square
"""


class Square:
    """A Square is a shape that has 4 sides of equal length

    Attributes:
       size (int): The length of each edge of a Square
    """
    def __init__(self, size=0):
        """The initialization of a Square

        Args:
            size (int): The length of a Square's edge
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
