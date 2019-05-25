#!/usr/bin/python3
import numpy as np
"""Function to multiply two matrices."""


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: First matrix - must be a list of lists of ints or floats.
        m_b: Second matrix - must be a list of lists of ints or floats.

    Raises:
        TypeError: raised if input is incorrect.
        ValueError: raised if values of input is incorrect.
    """

    recA = []
    recB = []
    if type(m_a) is not list:
        raise TypeError
    if type(m_b) is not list:
        raise TypeError
    for x in m_a:
        recA.append(len(x))
        if type(x) is not list:
            raise TypeError
        elif len(x) == 0:
            raise ValueError
    for x in m_b:
        recB.append(len(x))
        if type(x) is not list:
            raise TypeError
        elif len(x) == 0:
            raise ValueError
    if len(m_a) == 0:
        raise ValueError
    if len(m_b) == 0:
        raise ValueError
    for row in m_a:
        for value in row:
            if type(value) is not int or type(value) is not float:
                raise TypeError
    for row in m_b:
        for value in row:
            if type(value) is not int or type(value) is not float:
                raise TypeError
    if len(set(recA)) != 1:
        raise TypeError
    if len(set(recB)) != 1:
        raise TypeError
    a = np.array(m_a)
    b = np.array(m_b)
    return (np.dot(a, b))
