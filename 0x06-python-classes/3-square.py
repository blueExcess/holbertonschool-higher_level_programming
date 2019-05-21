#!/usr/bin/python3
class Square:
    """Class square with one attribute.

    Args:
        size (int): size of square. Must be int.

    Raises:
        TypeError: given value not int
        ValueError: given int not above 0
    """
    def __init__(self, size=0):
        """Inits class with given size."""
        self.__size = size
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        """Calculates area of square.

        Return:
            Area of square object.
        """
        return self.__size ** 2
