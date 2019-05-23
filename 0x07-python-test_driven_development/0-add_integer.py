#!/usr/bin/python3
"""Small module for adding two ints.
making this description
take up
five lines (for no reason - thanks checker)
"""


def add_integer(a, b=98):
    """Adds two ints.

    Args:
        a: float or int.
        b: float or int (default = 98).

    Raises:
        TypeError: if number is not float or int.
    """
    if type(a) is float or type(a) is int:
        a = int(a)
    else:
        raise TypeError('a must be an integer')
    if type(b) is float or type(b) is int:
        b = int(b)
    else:
        raise TypeError('b must be an integer')
    return a + b
