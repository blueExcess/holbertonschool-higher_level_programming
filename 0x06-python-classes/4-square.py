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

    @property
    def size(self):
        """Getter function to return size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function to set size value.

        Raises:
            TypeError: if value is not int.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
