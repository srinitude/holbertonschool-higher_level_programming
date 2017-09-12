#!/usr/bin/python3
"""
Unit tests for Rectangle class
"""


import unittest
from models import rectangle
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    """Presence of docstrings"""
    def test_presence_of_module_docstring(self):
        module_doc = rectangle.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        class_doc = Rectangle.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        init_doc = Rectangle.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)

    def test_presence_of_str_docstring(self):
        str_doc = Rectangle.__str__.__doc__
        self.assertTrue(len(str_doc) > 1)

    def test_presence_of_width_docstring(self):
        width_doc = Rectangle.width.__doc__
        self.assertTrue(len(width_doc) > 1)

    def test_presence_of_height_docstring(self):
        height_doc = Rectangle.height.__doc__
        self.assertTrue(len(height_doc) > 1)

    def test_presence_of_x_docstring(self):
        x_doc = Rectangle.x.__doc__
        self.assertTrue(len(x_doc) > 1)

    def test_presence_of_y_docstring(self):
        y_doc = Rectangle.y.__doc__
        self.assertTrue(len(y_doc) > 1)

    def test_presence_of_area_docstring(self):
        area_doc = Rectangle.area.__doc__
        self.assertTrue(len(area_doc) > 1)

    def test_presence_of_display_doc(self):
        disp_doc = Rectangle.display.__doc__
        self.assertTrue(len(disp_doc) > 1)

    def test_presence_of_update_doc(self):
        up_doc = Rectangle.update.__doc__
        self.assertTrue(len(up_doc) > 1)

    def test_presence_of_to_dict_doc(self):
        td_doc = Rectangle.to_dictionary.__doc__
        self.assertTrue(len(td_doc) > 1)

    def test_rect_id(self):
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(10, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r1.id, 1)
        self.assertEqual(r2.id, 2)
        self.assertEqual(r3.id, 12)

    """Initialization tests with valid arguments"""
    def test_all_valid_params(self):
        Rectangle._Base__nb_object = 0
        self.rect = Rectangle(10, 2, 3, 4, 12)
        self.assertEqual(self.rect.id, 12)
        self.assertEqual(self.rect.x, 3)
        self.assertEqual(self.rect.y, 4)
        self.assertEqual(self.rect.width, 10)
        self.assertEqual(self.rect.height, 2)

    """Initialization tests with invalid arguments"""
    def test_bad_height(self):
        Rectangle._Base__nb_object = 0
        with self.assertRaises(TypeError, msg="height must be an integer"):
            self.rect = Rectangle(10, "2")

    def test_bad_width(self):
        Rectangle._Base__nb_object = 0
        with self.assertRaises(ValueError, msg="width must be > 0"):
            self.rect = Rectangle(-10, 2)

    def test_bad_x(self):
        Rectangle._Base__nb_object = 0
        with self.assertRaises(TypeError, msg="x must be an integer"):
            self.rect = Rectangle(10, 2, {})

    def test_bad_y(self):
        Rectangle._Base__nb_object = 0
        with self.assertRaises(ValueError, msg="y must be >= 0"):
            self.rect = Rectangle(10, 2, 3, -1)

    """Area"""
    def test_area(self):
        Rectangle._Base__nb_object = 0
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    """Display"""
    def test_display_at_origin(self):
        self.rect = Rectangle(4, 6)

if __name__ == "__main__":
    unittest.main()
