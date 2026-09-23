#!/usr/bin/python3
"""Test max_integer."""

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Test cases for max_integer."""

    def test_positive(self):
        """Test positive numbers."""
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_negative(self):
        """Test negative numbers."""
        self.assertEqual(max_integer([-1, -2, -3]), -1)

    def test_empty(self):
        """Test empty list."""
        self.assertIsNone(max_integer([]))

    def test_one(self):
        """Test one element."""
        self.assertEqual(max_integer([5]), 5)

    def test_unsorted(self):
        """Test unsorted list."""
        self.assertEqual(max_integer([4, 1, 7, 2]), 7)


if __name__ == '__main__':
    unittest.main()
