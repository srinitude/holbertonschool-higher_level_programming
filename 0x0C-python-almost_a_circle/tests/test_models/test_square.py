#!/usr/bin/python3
"""
Unit tests for Square class
"""


import unittest
from models.base import Base
from models import square
from models.square import Square


class TestSquare(unittest.TestCase):
    """Square tests"""
    def test_presence_of_module_docstring(self):
        """Presence of docstrings"""
        module_doc = square.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        """Presence of docstrings"""
        class_doc = Square.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        """Presence of docstrings"""
        init_doc = Square.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)

    def test_presence_of_str_docstring(self):
        """Presence of docstrings"""
        str_doc = Square.__str__.__doc__
        self.assertTrue(len(str_doc) > 1)

    def test_presence_of_size_doc(self):
        """Presence of docstrings"""
        size_doc = Square.size.__doc__
        self.assertTrue(len(size_doc) > 1)

    def test_presence_of_update_doc(self):
        """Presence of docstrings"""
        up_doc = Square.update.__doc__
        self.assertTrue(len(up_doc) > 1)

    def test_presence_of_to_dict_doc(self):
        """Presence of docstrings"""
        td_doc = Square.to_dictionary.__doc__
        self.assertTrue(len(td_doc) > 1)

    def test_all_valid_params(self):
        """Initialization tests with valid arguments"""
        Base._Base__nb_objects = 0
        self.sq = Square(10, 3, 4, 12)
        self.assertEqual(self.sq.x, 3)
        self.assertEqual(self.sq.y, 4)
        self.assertEqual(self.sq.size, 10)

    def test_bad_size_type(self):
        """Initialization tests with invalid arguments"""
        with self.assertRaises(TypeError) as cm:
            self.sq = Square("10")

    def test_bad_size_value(self):
        """Initialization tests with invalid arguments"""
        with self.assertRaises(ValueError) as cm:
            self.sq = Square(-10)

    def test_bad_x(self):
        """Initialization tests with invalid arguments"""
        with self.assertRaises(TypeError) as cm:
            self.sq = Square(10, {})

    def test_bad_y(self):
        """Initialization tests with invalid arguments"""
        with self.assertRaises(ValueError) as cm:
            self.sq = Square(10, 3, -1)

    def test_area(self):
        """Area"""
        Base._Base__nb_objects = 0
        sq1 = Square(6)
        sq2 = Square(5, 1, 2)
        sq3 = Square(7, 1, 7, 12)
        self.assertEqual(sq1.area(), 36)
        self.assertEqual(sq2.area(), 25)
        self.assertEqual(sq3.area(), 49)

if __name__ == "__main__":
    unittest.main()
