#!/usr/bin/python3
"""
This module describes the perfect Student
"""


class Student:
    """
    Here's the layout of a Student
    """
    def __init__(self, first_name, last_name, age):
        """
        Initialization of a Student

        Args:
            first_name (str): The Student's first name
            last_name (str): The Student's last name
            age (int): The Student's age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        The dictionary representation of a Student

        Args:
            attrs (list): List of attributes to retrieve
        """
        if not attrs:
            return self.__dict__
        attr_dict = {}
        for attr in attrs:
            if attr in self.__dict__:
                attr_dict[attr] = self.__dict__[attr]
        return attr_dict
