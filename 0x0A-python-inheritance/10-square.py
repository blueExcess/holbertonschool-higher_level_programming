#!/usr/bin/python3
"""Classes all about shapes! Huzzah!"""


class BaseGeometry():
    """A class that will do something, presumably.

    Raises:
        TypeError: if value is not int.
        ValueError: if value is 0 or less.
    """
    def area(self):
        """Calculates the area of obj. Not implemented."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates 'value' and raises exceptions for fun."""
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Class of shape.

    Args:
        width (int): width of rectangle.
        height (int): height of rectangle.

    Raises:
        TypeError: if value is not int.
        ValueError: if value is 0 or less.
    """

    def __init__(self, width, height):
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height

    def area(self):
        """Returns area of rectangle."""
        return self.__height * self.__width

    def __str__(self):
        """Return a different thing than normal. Yay!"""
        return "[Rectangle] {:d}/{:d}".format(self.__width, self.__height)

class Square(Rectangle):
    """A type of shape that's a bit... square.

    Args:
        size (int): length of height and width (as typical with squares).
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
