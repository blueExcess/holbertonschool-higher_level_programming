#!/usr/bin/python3
"""Module for dividing everything in a matrix by something."""


def matrix_divided(matrix, div):
    """Divide everything in matrix by div.

    Args:
        matrix: matrix is list of lists, must be ints or floats.
        div: must be int or float

    Raises:
        TypeError: Must be a matrix and have consistant size.
        ZeroDivisionError: div == 0 (fail).
    """
    m1 = "matrix must be a matrix (list of lists) of integers/floats"
    size = []
    if len(matrix) == 0:
        raise TypeError(m1)
    for row in matrix:
        if len(row) == 0:
            raise TypeError(m1)
        else:
            size.append(len(row))
        for x in row:
            if type(x) is not float and type(x) is not int:
                raise TypeError(m1)
    if len(set(size)) != 1:
        raise TypeError('Each row of the matrix must have the same size')
    if type(div) is float or type(div) is int:
        pass
    else:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')
    return [[round(x/div, 2) for x in val] for val in matrix]
