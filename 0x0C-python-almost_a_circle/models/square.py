#!/usr/bin/python3
"""Model for squares."""


from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter for size."""
        return self.width

    @size.setter
    def size(self, value):
        """Setter for size - based off width and height."""
        self.width = value
        self.height = value

    def __str__(self):
        """Return the proper string."""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

    def update(self, *args, **kwargs):
        """To update attributes in class."""
        i = 0
        for value in args:
            i += 1
            if i == 1:
                self.id = value
            if i == 2:
                self.size = value
            if i == 3:
                self.x = value
            if i == 4:
                self.y = value
        accepted = ['id', 'size', 'x', 'y']
        if len(args) == 0:
            for k, v in kwargs.items():
                if k in accepted:
                    setattr(self, k, v)

    def to_dictionary(self):
        """Returns a dict representation of object for json use."""
        a = {'id':self.id, 'size':self.size, 'x':self.x, 'y':self.y}
        return a
