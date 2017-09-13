#!/usr/bin/python3
"""
Unit tests for Base class
"""


import unittest
from models import base
from models.base import Base


class TestBase(unittest.TestCase):
    """Base class tests"""
    def test_presence_of_module_docstring(self):
        """Presence of module docstring"""
        module_doc = base.__doc__
        self.assertTrue(len(module_doc) > 1)

    def test_presence_of_class_docstring(self):
        """Presence of class docstring"""
        class_doc = Base.__doc__
        self.assertTrue(len(class_doc) > 1)

    def test_presence_of_init_docstring(self):
        """Presence of init docstring"""
        init_doc = Base.__init__.__doc__
        self.assertTrue(len(init_doc) > 1)

    def test_presence_of_to_json_docstring(self):
        """Presence of to json docstring"""
        to_js_doc = Base.to_json_string.__doc__
        self.assertTrue(len(to_js_doc) > 1)

    def test_presence_of_from_json_docstring(self):
        """Presence of from json docstring"""
        f_js_doc = Base.from_json_string.__doc__
        self.assertTrue(len(f_js_doc) > 1)

    def test_presence_of_save_to_file_docstr(self):
        """Presence of save to file docstring"""
        stf_doc = Base.save_to_file.__doc__
        self.assertTrue(len(stf_doc) > 1)

    def test_presence_of_create_docstring(self):
        """Presence of create docstring"""
        c_doc = Base.create.__doc__
        self.assertTrue(len(c_doc) > 1)

    def test_presence_of_load_from_file_docstr(self):
        """Presence of load from file docstring"""
        lff_doc = Base.load_from_file.__doc__
        self.assertTrue(len(lff_doc) > 1)

    def test_ids(self):
        """Testing correct ids"""
        Base._Base__nb_objects = 0
        self.b1 = Base()
        self.b2 = Base()
        self.b3 = Base()
        self.b4 = Base(12)
        self.b5 = Base()

        self.assertEqual(self.b1.id, 1)
        self.assertEqual(self.b2.id, 2)
        self.assertEqual(self.b3.id, 3)
        self.assertEqual(self.b4.id, 12)
        self.assertEqual(self.b5.id, 4)

if __name__ == "__main__":
    unittest.main()
