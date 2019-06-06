#!/usr/bin/python3
"""11. Class for Student that does stuff."""


class Student():
    """does json type stuff.

    Args:
        first_name (str): first name of student.
        last_name (str): last name of student.
        age (int): age of student.
    """

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns __dict__ of object."""
        x = self.__dict__
        if not attrs is None:
            for k, v in x:
                if k in attrs:
                    
