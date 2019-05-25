#!/usr/bin/python3
"""Function to multiply two matrices."""


def matrix_mul(m_a, m_b):
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
        raise TypeError('m_a must be a list')
    if type(m_b) is not list:
        raise TypeError('m_b must be a list')
    for x in m_a:
        recA.append(len(x))
        if type(x) is not list:
            raise TypeError('m_a must be a list of lists')
        elif len(x) == 0:
            raise ValueError("m_a can't be empty")
    for x in m_b:
        recB.append(len(x))
        if type(x) is not list:
            raise TypeError('m_b must be a list of lists')
        elif len(x) == 0:
            raise ValueError("m_b can't be empty")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        for value in row:
            if type(value) is not int or type(value) is not float:
                raise TypeError('m_a should contain only integers or floats')
    for row in m_b:
        for value in row:
            if type(value) is not int or type(value) is not float:
                raise TypeError('m_b should contain only integers or floats')
    if len(set(recA)) != 1:
        raise TypeError("each row of m_a must should be of the same size")
    if len(set(recB)) != 1:
        raise TypeError("each row of m_b must should be of the same size")

    if len(m_a) != len(m_b[0]) or len(m_a[0]) != len(m_b):
        raise ValueError('m_a and m_b can't be multiplied')
    for row in m_a:
