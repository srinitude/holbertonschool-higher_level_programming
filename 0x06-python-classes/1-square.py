#!/usr/bin/python3
"""
This module contains documentation for a Square
"""

class Square:
    """A Square is a shape that has 4 sides of equal length

    Attributes:
        __size (int): The length of each edge of a Square
    """
    def __init__(self, size):
        """The initialization of a Square

        Args:
            size (int): The length of a Square's edge
        """
        self.__size = size
