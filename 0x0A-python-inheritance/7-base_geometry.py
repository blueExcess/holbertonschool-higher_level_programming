#!/usr/bin/python3
"""Class that does something."""


class BaseGeometry():
    """A class that will do something, presumably."""
    def area(self):
        """Calculates the area of obj. Not implemented."""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """validates 'value' and raises exceptions for fun."""
        if not type(value) is int:
            raise TypeError('{} must be an integer'.format(name))
        elif value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
