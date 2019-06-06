#!/usr/bin/python3
"""Contains class to do annoying things."""


class MyInt(int):
    """Will switch around the == and != operators. Tee hee hee."""

    def __eq__(self, value):
        """Return wrong operator."""
        return super().__ne__(self)

    def __ne__(self, value):
        """Returns the equals operator."""
        return super().__eq__(self)
