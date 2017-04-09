# -*- coding: utf-8 -*-
"""Unittest for a flatten arrays.

Example:
        $ python nested_arrays_test.py
"""
import unittest
from nested_arrays import processor_nested_arrays


class TestStringMethods(unittest.TestCase):
    """Class of nested_arrays using unittest.
    """

    def test_proposed(self):
        """Using nested array proposed.
        """
        my_array = [[1, 2, [3]], 4]
        self.assertEqual([1, 2, 3, 4], processor_nested_arrays(narrays=my_array))

    def test_other_option(self):
        """Using other nested array.
        """
        other = [[1, 2, [3]], [4, [5], 6]]
        self.assertEqual([1, 2, 3, 4, 5, 6], processor_nested_arrays(narrays=other))

    def test_blank(self):
        """Using a blank nested array.
        """
        blank = []
        self.assertEqual([], processor_nested_arrays(narrays=blank))

    def test_type(self):
        """Check if function return a list.
        """
        blank = []
        self.assertTrue(type(processor_nested_arrays(narrays=blank) is list))



if __name__ == '__main__':
    unittest.main()
