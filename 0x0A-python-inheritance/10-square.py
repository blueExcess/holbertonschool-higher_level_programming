#!/usr/bin/python3
"""Classes all about shapes! Huzzah!"""


Square = __import__('10-square').Square
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A type of shape that's a bit... square.

    Args:
        size (int): length of height and width (as typical with squares).
    """

    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
