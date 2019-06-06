#!/usr/bin/python3
"""Adds a function to attempt to add attributes to objects."""


def add_attribute(obj, name, value):
    """Attempts to add a value to an object.

    Args:
        obj: object to attempt to add to.
        name (str): name of attribute to add.
        value: value to add.

    Raises:
        TypeError: if obj can't accept new attributes.
    """

    if hasattr(obj, '__dict__') and not hasattr(obj, '__slots__'):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
