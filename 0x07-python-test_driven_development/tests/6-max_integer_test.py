#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    def test_empty_list(self):
        empty_list = []
        self.assertIsNone(max_integer(empty_list))

    def test_one_element(self):
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_some_elements(self):
        some_elements = [3425, 457458, 1, 3249056, -2346, 0]
        self.assertEqual(max_integer(some_elements), 3249056)

if __name__ == "__main__":
    unittest.main()
