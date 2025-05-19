#!/usr/bin/python3
"""
    Unittest for max_integer([..])
"""
import unittest
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """TestCase class for testing the max_integer function"""

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))
        self.assertIsNone(max_integer())

    def test_single_element(self):
        """Test list with a single element"""
        self.assertEqual(max_integer([5]), 5)
        self.assertEqual(max_integer([-10]), -10)
        self.assertEqual(max_integer([0]), 0)

    def test_positive_numbers(self):
        """Test list with only positive numbers"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)
        self.assertEqual(max_integer([10, 9, 8, 7]), 10)

    def test_negative_numbers(self):
        """Test list with only negative numbers"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -3, -2, -1]), -1)
        self.assertEqual(max_integer([-7, -5, -9, -2]), -2)

    def test_mixed_numbers(self):
        """Test list with mixed positive and negative numbers"""
        self.assertEqual(max_integer([-1, 2, -3, 4]), 4)
        self.assertEqual(max_integer([5, -6, 7, -8]), 7)
        self.assertEqual(max_integer([-10, 0, 10]), 10)

    def test_duplicates(self):
        """Test list with duplicate values"""
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)
        self.assertEqual(max_integer([1, 5, 5, 3]), 5)
        self.assertEqual(max_integer([7, 7, 2, 7]), 7)

    def test_max_at_beginning(self):
        """Test with maximum value at the beginning"""
        self.assertEqual(max_integer([5, 4, 3, 2, 1]), 5)
        self.assertEqual(max_integer([8, 4, 6, 2]), 8)

    def test_max_in_middle(self):
        """Test with maximum value in the middle"""
        self.assertEqual(max_integer([1, 3, 5, 2, 4]), 5)
        self.assertEqual(max_integer([2, 4, 8, 6]), 8)

    def test_max_at_end(self):
        """Test with maximum value at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([2, 4, 6, 8]), 8)

    def test_large_numbers(self):
        """Test with very large integers"""
        self.assertEqual(max_integer([1000000, 10000000, 100000000]), 100000000)
        self.assertEqual(max_integer([2**31 - 1, 2**31 - 2]), 2**31 - 1)

    def test_floats(self):
        """Test with floating point numbers"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5]), 3.5)
        self.assertEqual(max_integer([-2.2, -1.1, -3.3]), -1.1)
        self.assertEqual(max_integer([1, 2.5, 3]), 3)

    def test_strings(self):
        """Test with strings (should compare lexicographically)"""
        self.assertEqual(max_integer(["a", "b", "c"]), "c")
        self.assertEqual(max_integer(["apple", "banana", "cherry"]), "cherry")
        self.assertEqual(max_integer(["z", "y", "x"]), "z")

    def test_list_of_lists(self):
        """Test with list of lists"""
        self.assertEqual(max_integer([[1, 2], [3, 4]]), [3, 4])
        self.assertEqual(max_integer([[5], [3], [7]]), [7])

    def test_list_of_tuples(self):
        """Test with list of tuples"""
        self.assertEqual(max_integer([(1, 2), (3, 4)]), (3, 4))
        self.assertEqual(max_integer([(5, 0), (3, 9), (7, 5)]), (7, 5))


if __name__ == '__main__':
    unittest.main()