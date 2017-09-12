#!/usr/bin/python3
"""
Unit tests for Square class
"""


import unittest
from models import square
from models.square import Square


class TestSquare(unittest.TestCase):
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

    """Initialization tests with valid arguments"""
    def test_all_valid_params(self):
        self.sq = Square(10, 3, 4, 12)
        self.assertEqual(self.sq.x, 3)
        self.assertEqual(self.sq.y, 4)
        self.assertEqual(self.sq.size, 10)

    """Initialization tests with invalid arguments"""
    def test_bad_size_type(self):
        with self.assertRaises(TypeError) as cm:
            self.sq = Square("10")

    def test_bad_size_value(self):
        with self.assertRaises(ValueError) as cm:
            self.sq = Square(-10)

    def test_bad_x(self):
        with self.assertRaises(TypeError) as cm:
            self.sq = Square(10, {})

    def test_bad_y(self):
        with self.assertRaises(ValueError) as cm:
            self.sq = Square(10, 3, -1)

    """Area"""
    def test_area(self):
        self.sq = Square(6)
        self.assertEqual(self.sq.area(), 36)

if __name__ == "__main__":
    unittest.main()
