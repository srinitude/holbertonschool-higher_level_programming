#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""


import unittest
import sys
from models.base import Base
from models import rectangle
from models.rectangle import Rectangle
from io import StringIO


class TestRectangle(unittest.TestCase):
    """Rectangle tests"""
    def test_presence_of_module_docstring(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        module_doc = rectangle.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        class_doc = Rectangle.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        init_doc = Rectangle.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)

    def test_presence_of_str_docstring(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        str_doc = Rectangle.__str__.__doc__
        self.assertTrue(len(str_doc) > 1)

    def test_presence_of_width_docstring(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        width_doc = Rectangle.width.__doc__
        self.assertTrue(len(width_doc) > 1)

    def test_presence_of_height_docstring(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        height_doc = Rectangle.height.__doc__
        self.assertTrue(len(height_doc) > 1)

    def test_presence_of_x_docstring(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        x_doc = Rectangle.x.__doc__
        self.assertTrue(len(x_doc) > 1)

    def test_presence_of_y_docstring(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        y_doc = Rectangle.y.__doc__
        self.assertTrue(len(y_doc) > 1)

    def test_presence_of_area_docstring(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        area_doc = Rectangle.area.__doc__
        self.assertTrue(len(area_doc) > 1)

    def test_presence_of_display_doc(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        disp_doc = Rectangle.display.__doc__
        self.assertTrue(len(disp_doc) > 1)

    def test_presence_of_update_doc(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        up_doc = Rectangle.update.__doc__
        self.assertTrue(len(up_doc) > 1)

    def test_presence_of_to_dict_doc(self):
        """Presence of docstrings"""
        Base._Base__nb_objects = 0
        td_doc = Rectangle.to_dictionary.__doc__
        self.assertTrue(len(td_doc) > 1)

    def test_rect_id(self):
        """Id checking"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_all_valid_params(self):
        """Initialization tests with valid arguments"""
        Base._Base__nb_object = 0
        self.rect = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(self.rect.id, 12)
        self.assertEqual(self.rect.x, 3)
        self.assertEqual(self.rect.y, 4)
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 2)

    def test_bad_height(self):
        """Initialization tests with invalid arguments"""
        Base._Base__nb_object = 0
        with self.assertRaises(TypeError, msg="height must be an integer"):
            self.rect = Rectangle(10, "2")

    def test_bad_width(self):
        """Initialization tests with invalid arguments"""
        Base._Base__nb_object = 0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.rect = Rectangle(-10, 2)

    def test_bad_x(self):
        """Initialization tests with invalid arguments"""
        Base._Base__nb_object = 0
        with self.assertRaises(TypeError, msg="x must be an integer"):
            self.rect = Rectangle(10, 2, {})

    def test_bad_y(self):
        """Initialization tests with invalid arguments"""
        Base._Base__nb_object = 0
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            self.rect = Rectangle(10, 2, 3, -1)

    def test_area(self):
        """Test area"""
        Base._Base__nb_object = 0
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_display_at_origin(self):
        """Test display at origin"""
        Base._Base__nb_object = 0
        r1 = Rectangle(10, 2)
        my_stdout = StringIO()
        sys.stdout = my_stdout
        r1.display()
        sys.stdout = sys.__stdout__
        expected = "##########\n##########\n"
        self.assertEqual(expected, my_stdout.getvalue())

    def test_display_not_at_origin(self):
        """Test display not at origin"""
        Base._Base__nb_object = 0
        r1 = Rectangle(2, 3, 2, 2)
        my_stdout = StringIO()
        sys.stdout = my_stdout
        r1.display()
        sys.stdout = sys.__stdout__
        expected = "\n\n  ##\n  ##\n  ##\n"
        self.assertEqual(expected, my_stdout.getvalue())

if __name__ == "__main__":
    unittest.main()
