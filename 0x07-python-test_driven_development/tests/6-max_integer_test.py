#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Working results"""
    def test_empty_list(self):
        empty_list = []
        self.assertIsNone(max_integer(empty_list))

    def test_no_arguments(self):
        self.assertIsNone(max_integer())

    def test_one_element(self):
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_some_elements(self):
        some_elements = [3425, 457458, 1, 3249056, -2346, 0]
        self.assertEqual(max_integer(some_elements), 3249056)

    def test_floats(self):
        list_with_floats = [23.2354, 635.34, 234658, 99, -102346.052]
        self.assertEqual(max_integer(list_with_floats), 234658)

    """Catching exceptions"""
    def test_passing_none(self):
        with self.assertRaises(TypeError):
            max_integer(None)

    def test_passing_string(self):
        string_in_list = [2345, 2, "L0Lz", 9]
        with self.assertRaises(TypeError):
            max_integer(string_in_list)

if __name__ == "__main__":
    unittest.main()
