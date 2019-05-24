#!/usr/bin/python3
"""Function to print square with character '#'."""


def print_square(size):
    """Print a square (size by size) with char '#'

    Args:
        size (int): size of square (num of '#' per row).

    Raises:
        TypeError: size must be an int.
        ValueError: size must be > 0.
    """

    if not isinstance(size, int):
        raise TypeError('size must be an integer')
    elif size < 0:
        raise ValueError('size must be >= 0')
    else:
        for x in range(size):
            print('#' * size)
