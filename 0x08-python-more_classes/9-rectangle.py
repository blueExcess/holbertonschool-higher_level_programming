#!/usr/bin/python3
"""Module to create a rectangle class and methods."""


class Rectangle():
    """Class used to create Rectangle objects.

    Attributes:
        number_of_instances: number of instances currently existing
        print_symbol: used for string representation, default = #.

    Args:
        width (int): width of the rectangle.
        height (int): height of the rectangle.

    Raises:
        TypeError: If given value is not an int.
        ValueError: If given value is < 0.
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width param."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width param."""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height param."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height param."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """Return area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle - or 0 if either value is 0."""
        if self.width == 0 or self.height == 0:
            return 0
        else:
            return self.width + self.height

    def __str__(self):
        """Print out a visualization of the rectangle."""
        out = []
        if self.width == 0 or self.height == 0:
            return ""
        for _ in range(self.height):
            out.append(str(self.print_symbol) * self.width)
        return "\n".join(out)

    def __repr__(self):
        """For returning something silly."""
        return "{}({}, {})".format(type(self).__name__,
                                   self.width, self.height)

    def __del__(self):
        """What happens when object is deleted."""
        print('Bye rectangle...')
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Static method to compare two rectangle object's size."""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        elif not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        else:
            return rect_1 if rect_1.area() >= rect_2.area() else rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
