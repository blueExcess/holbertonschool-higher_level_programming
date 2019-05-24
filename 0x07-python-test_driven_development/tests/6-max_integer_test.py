#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Class for testing max_integer things."""

    te_m = "'>' not supported between instances of 'str' and 'int'"
    def test_std_behavior(self):
        """Test standard behavior."""
        a = [1, 2, 3]
        self.assertEqual(max_integer(a), 3)

    def test_negatives(self):
        """Works with negative numbers."""
        self.assertEqual(max_integer([-3, 5, -2]), 5)

    def test_floats(self):
        """Works with mixed floats and ints."""
        self.assertEqual(max_integer([2.94, 1, 8.493]), 8.493)

    def test_multi_lists(self):
        """Works with lists of lists."""
        a = [1, 2, 3]
        b = [1, 9, 3]
        c = [4, 2, 1]
        d = [a, b, c]
        self.assertEqual(max_integer(d), [4, 2, 1])

    def test_tuples(self):
        """Works with tuples."""
        self.assertEqual(max_integer((8, 3, 12)), 12)

    @unittest.expectedFailure
    def test_sets(self):
        """Doesn't work with sets."""
        a = [3, 3, 9, 2, 8, 6, 9, 0, 1]
        self.assertEqual(max_integer(set(a)), 9)

    @unittest.expectedFailure
    def test_dicts(self):
        """Doesn't work with dicts."""
        a = {1:2, 3:4, 5:6}
        self.assertEqual(max_integer(a), 5)

    def test_wrong_type(self):
        """Throws error for incorrect type."""
        a = [1, 2, 'd', 3]
        with self.assertRaises(TypeError, msg=self.te_m):
            max_integer(a)
