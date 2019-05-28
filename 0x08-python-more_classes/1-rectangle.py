#!/usr/bin/python3
"""Module to create a rectangle class and methods."""


class Rectangle():
    """Class used to create Rectangle objects.

    Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.

    Raises:
        TypeError: If given value is not an int.
        ValueError: If given value is < 0.
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value
