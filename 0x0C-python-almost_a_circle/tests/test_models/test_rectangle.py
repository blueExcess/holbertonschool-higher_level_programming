#!/usr/bin/python3
"""Unittests for Rectangle model."""


import unittest
from models.rectangle import Rectangle


class Test_Rectangle(unittest.TestCase):
    """Class for testing various aspects of the Rectangle model."""
    def setUp(self):
        Rectangle._Base__nb_objects = 0

    def test_init(self):
        a = Rectangle(2, 3)
        self.assertEqual(a.width, 2)
        self.assertEqual(a.height, 3)
        self.assertEqual(a.x, 0)
        self.assertEqual(a.y, 0)
        self.assertEqual(a.id, 1)
        b = Rectangle(5, 1, 9, 2)
        self.assertEqual(b.width, 5)
        self.assertEqual(b.height, 1)
        self.assertEqual(b.x, 9)
        self.assertEqual(b.y, 2)
        self.assertEqual(b.id, 2)
        c = Rectangle(23, 4, 2, 5, 12)
        self.assertEqual(c.width, 23)
        self.assertEqual(c.height, 4)
        self.assertEqual(c.x, 2)
        self.assertEqual(c.y, 5)
        self.assertEqual(c.id, 12)
        d = Rectangle(6, 9, 3)
        self.assertEqual(d.width, 6)
        self.assertEqual(d.height, 9)
        self.assertEqual(d.x, 3)
        self.assertEqual(d.y, 0)
        self.assertEqual(d.id, 3)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            e = Rectangle("hi", 3)
        with self.assertRaises(ValueError, msg='width must be > 0'):
            f = Rectangle(-8, 4)
        with self.assertRaises(TypeError, msg='width must be an integer'):
            g = Rectangle([1, 2, 3], 4)
        with self.assertRaises(TypeError, msg='height must be an integer'):
            h = Rectangle(9, "bob")
        with self.assertRaises(TypeError, msg='height must be an integer'):
            i = Rectangle(14, [8, 4])
        with self.assertRaises(TypeError, msg='height must be an integer'):
            j = Rectangle(3, (4, 1))
        with self.assertRaises(ValueError, msg='height must be > 0'):
            k = Rectangle(4, -9)
        with self.assertRaises(TypeError, msg='x must be an integer'):
            l = Rectangle(2, 3, "hi")
        with self.assertRaises(TypeError, msg='x must be an integer'):
            m = Rectangle(5, 3, [1, 2])
        with self.assertRaises(TypeError, msg='x must be an integer'):
            n = Rectangle(2, 5, float(8))
        with self.assertRaises(ValueError, msg='x must be > 0'):
            o = Rectangle(1, 8, -3)
        with self.assertRaises(TypeError, msg='y must be an integer'):
            p = Rectangle(5, 4, 3, "hi")
        with self.assertRaises(TypeError, msg='y must be an integer'):
            q = Rectangle(33, 1, 19, set([1, 22, 2, 2]))
        with self.assertRaises(ValueError, msg='y must be > 0'):
            r = Rectangle(3, 1, 8, -14)
