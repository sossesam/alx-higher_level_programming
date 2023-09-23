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

    def update(self, *args, **kwargs):
        """
        This function assigns values and attributes
        """
        if len(args):
            for i, j in enumerate(args):
                if i == 0:
                    self.id = j
                if i == 1:
                    self.size = j
                if i == 2:
                    self.x = j
                if i == 3:
                    self.y = j
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]

    def to_dictionary(self):
        """
        This modules contains a class rectangle
        with all its methods and attributes
        definition
        """
        dict = {}
        dict['x'] = self.x
        dict['y'] = self.y
        dict["size"] = self.width
        dict["id"] = self.id

        return dict
