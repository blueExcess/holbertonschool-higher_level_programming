#!/usr/bin/python3
"""Model for squares."""


from models.base import Base
from models.rectangle import Rectangle

class Square(Rectangle):
    """Square class."""

    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the proper string."""
        return "[{}] ({}) {}/{} - {}".format(type(self).__name__, self.id,
                                             self.x, self.y, self.width)

        
