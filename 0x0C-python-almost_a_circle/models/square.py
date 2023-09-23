#!/usr/bin/python3
"""
This modules contains a class rectangle
with all its methods and attributes
definition
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    This modules contains a class rectangle
    with all its methods and attributes
    definition
    """

    def __init__(self, size, x=0, y=0, id=None):
        """
        This modules contains a class rectangle
        with all its methods and attributes
        definition
        """
        self.width = size
        self.height = size
        self.x = x
        self.y = y
        self.id = id

        super().__init__(self.width, self.height, self.x, self.y, self.id)

    def __str__(self):
        """
        This modules contains a class rectangle
        with all its methods and attributes
        definition
        """
        name = type(self).__name__
        id = self.id
        x = self.x
        y = self.y
        return f"[{name}] ({id}) {x}/{y} - {self.width}"

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, size):
        self.width = size
        self.height = size
