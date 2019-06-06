#!/usr/bin/python3
"""Classes all about shapes! Huzzah!"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


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
