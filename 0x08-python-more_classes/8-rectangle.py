#!/usr/bin/python3
"""
Here's an implementation of a Rectangle
"""


class Rectangle:
    """
    Args:
        width (int): The width of the Rectangle
        height (int): The height of the Rectangle

    Class variables:
        number_of_instances (int):
            The number of Rectangles that have been instantiated
        print_symbol (any): The object(s) to be printed
    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        Initialization of a Rectangle after it gets instantiated

        Args:
            width (int): The width of the Rectangle
            height (int): The height of the Rectangle
        """
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    def __del__(self):
        """
        Deinitialization of a Rectangle after it gets deleted
        """
        type(self).number_of_instances -= 1
        print("Bye rectangle...")

    def __str__(self):
        """
        The user-friendly string representation of a Rectangle
        """
        if self.perimeter() == 0:
            return ""
        rec = ""
        for i in range(1, self.__height + 1):
            for j in range(1, self.__width + 1):
                rec += str(self.print_symbol)
            if i < self.__height:
                rec += "\n"
        return rec

    def __repr__(self):
        """
        The official string representation of a Rectangle
        """
        width = self.__width
        height = self.__height
        return "Rectangle({:d}, {:d})".format(width, height)

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

    def area(self):
        """
        Returns:
            The area of the Rectangle
        """
        return self.__height * self.__width

    def perimeter(self):
        """
        Returns:
            The perimeter of the Rectangle
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__height * 2) + (self.__width * 2)

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Returns:
            The biggest of two Rectangles

            If the first argument has an area equal to that
            of the second, the first Rectangle will be returned.
        """
        if type(rect_1) is not Rectangle:
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2) is not Rectangle:
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1 >= rect_2:
            return rect_1
        return rect_2

    def __ge__(self, other):
        return self.area() >= other.area()
