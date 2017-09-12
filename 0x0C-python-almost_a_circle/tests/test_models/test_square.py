#!/usr/bin/python3
"""
Unit tests for Square class
"""


import unittest
from models import square
from models.square import Square


class TestBase(unittest.TestCase):
    """Presence of docstrings"""
    def test_presence_of_module_docstring(self):
        module_doc = square.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        class_doc = Square.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        init_doc = Square.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)

    def test_presence_of_str_docstring(self):
        str_doc = Square.__str__.__doc__
        self.assertTrue(len(str_doc) > 1)

    def test_presence_of_size_doc(self):
        size_doc = Square.size.__doc__
        self.assertTrue(len(size_doc) > 1)

    def test_presence_of_update_doc(self):
        up_doc = Square.update.__doc__
        self.assertTrue(len(up_doc) > 1)

    def test_presence_of_to_dict_doc(self):
        td_doc = Square.to_dictionary.__doc__
        self.assertTrue(len(td_doc) > 1)

if __name__ == "__main__":
    unittest.main()
