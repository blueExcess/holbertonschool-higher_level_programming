#!/usr/bin/python3
""" some comment """
import math


class MagicClass:
    """Comment for class."""
    def __init__(self, radius=0):
        """comment for init"""
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """Def for Area stuff."""
        return self.__radius ** 2 * math.pi

    def circumference(self):
        """Def for this stuff."""
        return (2 * math.pi) * self.__radius
