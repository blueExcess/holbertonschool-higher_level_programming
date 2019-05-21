#!/usr/bin/python3
class Square:
    """Class square with one attribute.

    Args:
        size (int): size of square. Must be int.
        position (tuple): position for printing (my_print)

    Raises:
        TypeError: given value not int
        ValueError: given int not above 0
    """
    def __init__(self, size=0, position=(0, 0)):
        """Inits class with given size."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        if (isinstance(position, tuple) and len(position) == 2 and
                position[0] >= 0 and position[1] >= 0):
            self.__position = position
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position

    def area(self):
        """Calculates area of square.

        Return:
            Area of square object.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Return size value."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter function to set size value.

        Args:
            value (int): for setting the size of obj (must be int).

        Raises:
            TypeError: if value is not int.
            ValueError: if value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """Prints visualization of square to stdout with #."""
        value = self.__position
        x, y = value[0], value[1]
        for i in range(0, y):
            print()
        if self.__size == 0:
            print()
        else:
            for j in range(0, self.__size):
                print(' ' * x + '#' * self.__size)

    @property
    def position(self):
        """Returns the position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Sets position.

        Args:
            value (ints): tuple of two containing two ints, both > 0.

        Raises:
            TypeError: if tuple is not correct format
        """
        if (isinstance(value, tuple) and len(value) == 2 and
                value[0] >= 0 and value[1] >= 0):
            self.__position = value
        else:
            raise TypeError("position must be a tuple of 2 positive integers")
