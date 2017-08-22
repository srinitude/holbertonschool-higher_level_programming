#!/usr/bin/python3
"""
This module contains documentation for a Square
"""


class Square:
    """A Square is a shape that has 4 sides of equal length

    Attributes:
        __size (int): The length of each edge of a Square
    """
    def __init__(self, size=0):
        """The initialization of a Square

        Args:
            self (Square): The Sqaure instance
            size (int): The length of a Square's edge
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """
        Computes the area of the Square instance

        Args:
            self (Square): The square instance

        Returns: The area of the Square
        """
        return self.__size ** 2

    @property
    def size(self):
        """
        Getter for private __size attribute

        Args:
           self (Square): The square instance

        Returns:
           The size of the Square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        The setter for private __size attribute

        Args:
            self (Square): The Square instance
            value (int): The value to set private __size attribute to

        Returns:
            None
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """
        Prints the Square with the # character

        Args:
            self (Square): The Square instance

        Returns:
            None
        """
        if self.size == 0:
            print("")
            return
        for i in range(self.size):
            print("#" * self.size, end="")
            print("")
