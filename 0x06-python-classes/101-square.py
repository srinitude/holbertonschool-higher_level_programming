#!/usr/bin/python3
"""
This module contains documentation for a Square
"""


class Square:
    """A Square is a shape that has 4 sides of equal length

    Attributes:
        size (int): The length of each edge of a Square
        position (tuple): The coordinates of a Square in 2D space
    """
    def __init__(self, size=0, position=(0, 0)):
        """The initialization of a Square

        Args:
            self (Square): The Sqaure instance
            size (int): The length of a Square's edge
            position (tuple): Coordinates in 2D space
        """
        self.size = size
        self.position = position

    def __str__(self):
        """String representation of Square instance

        Args:
            self (Square): The Square instance
        """
        if self.size == 0:
            return ""
        output = ""
        x, y = self.position
        for i in range(y):
            output += "\n"
        for i in range(self.size):
            spaces = " " * x
            output += spaces
            content = "#" * self.size
            output += content
            if i < self.size - 1:
                output += "\n"
        return output


    def __repr__(self):
        """String representation of Square instance

        Args:
            self (Square): The Square instance
        """
        if self.size == 0:
            return ""
        output = ""
        x, y = self.position
        for i in range(y):
            output += "\n"
        for i in range(self.size):
            spaces = " " * x
            output += spaces
            content = "#" * self.size
            output += content
            if i < self.size - 1:
                output += "\n"
        return output

    def area(self):
        """
        Computes the area of the Square instance

        Args:
            self (Square): The square instance

        Returns:
            The area of the Square
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

    @property
    def position(self):
        """
        Getter for private __position attribute

        Args:
           self (Square): The square instance

        Returns:
           The position of the Square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        The setter for private __position attribute

        Args:
            self (Square): The Square instance
            value (tuple): The value to set private __position attribute to

        Returns:
            None
        """
        if type(value) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        if len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        x, y = value
        if (type(x) != int) or (type(y) != int) or (x < 0) or (y < 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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
        x, y = self.position
        for i in range(y):
            print("")
        for i in range(self.size):
            print(" " * x, end="")
            print("#" * self.size, end="")
            print("")
