#!/usr/bin/python3
"""Model for base."""


import json


class Base():
    """Base class."""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a list of dictionaries for fun and profit."""
        if list_dictionaries is None or len(list_dictionaries) == 0:
            a = '[]'
            return a
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Save instances to json file.

            Takes a string of dicts (that's been prepped for json) and saves it
        into a file named <class>.json. Guarenteed to make you rich!
        """
        if list_objs is None:
            js = cls.to_json_string('[]')
            with open(cls.__name__ + ".json", 'wt') as f:
                f.write(js)
        else:
            lis = []
            for x in list_objs:
                lis.append(x.to_dictionary())
            js = cls.to_json_string(lis)
            with open(cls.__name__ + ".json", 'wt') as f:
                f.write(js)
        return

    @staticmethod
    def from_json_string(json_string):
        """Takes a JSON string and turns it into a python object."""

        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)
