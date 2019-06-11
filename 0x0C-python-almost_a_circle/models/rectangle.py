#!/usr/bin/python3
"""Model for rectangles."""

from models.base import Base


class Rectangle(Base):
    """Rectangle class.

    Args:
        width (int): Width of the object.
        height (int): Height of the object.
        x (int): ?
        y (int): ?

    Raises:
        TypeError: If type of values is not int.
        ValueError: If value is outside bounds.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Getter for width."""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError('width must be > 0')
        else:
            self.__width = value

    @property
    def height(self):
        """Getter for height."""
        return self.__height

    @height.setter
    def height(self, value):
        """Setter for height."""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value <= 0:
            raise ValueError('height must be > 0')
        else:
            self.__height = value

    @property
    def x(self):
        """Getter for x."""
        return self.__x

    @x.setter
    def x(self, value):
        """Setter for x."""
        if type(value) is not int:
            raise TypeError('x must be an integer')
        elif value < 0:
            raise ValueError('x must be >= 0')
        else:
            self.__x = value

    @property
    def y(self):
        """Getter for y."""
        return self.__y

    @y.setter
    def y(self, value):
        """Setter for y."""
        if type(value) is not int:
            raise TypeError('y must be an integer')
        elif value < 0:
            raise ValueError('y must be >= 0')
        else:
            self.__y = value

    def area(self):
        """Return area of rectangle object."""
        return self.width * self.height

    def display(self):
        """Return a picture of the object."""
        print('\n' * self.y, end='')
        for _ in range(self.height):
            print(' ' * self.x + '#' * self.width)

    def __str__(self):
        """Return the proper thing."""
        return "[{}] ({}) {}/{} - {}/{}".format(type(self).__name__, self.id,
                                                self.x, self.y, self.width,
                                                self.height)

    def update(self, *args, **kwargs):
        """To update stuff."""
        i = 0
        for value in args:
            i += 1
            if i == 1:
                self.id = value
            if i == 2:
                self.width = value
            if i == 3:
                self.height = value
            if i == 4:
                self.x = value
            if i == 5:
                self.y = value
        accepted = ['id', 'width', 'height', 'x', 'y']
        if len(args) == 0:
            for k, v in kwargs.items():
                if k in accepted:
                    setattr(self, k, v)
