#!/usr/bin/python3
"""Unittests for base model."""


import io
import unittest
import importlib as il
from contextlib import redirect_stdout
from models.rectangle import Rectangle
from models.square import Square
from models.base import Base


class Test_Base(unittest.TestCase):
    """Class for testing base class."""

    def setUp(self):
        """Setup for reseting tests."""
        Base._Base__nb_objects = 0
        importlib.reload(models.square)
        importlib.reload(models.rectangle)
        importlib.reload(models.base)

    def test_to_json_string(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        s = '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]'
        self.assertEqual(s, print(json_dictionary))
        self.assertTrue(type(json_dictionary) is str)
