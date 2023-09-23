#!/usr/bin/python
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    pass
    """
    def __init__(self, size, x=0, y=0, id=None):
        self.__width = size
        self.__height = size
        self.x = x
        self.y = y
        self.id = id

        super().__init__(self.__width, self.__height, self.x, self.y, self.id)

    def __str__(self):
        name = type(self).__name__
        id = self.id
        x = self.x
        y = self.y
        return f"[{name}] ({id}) {x}/{y} - {self.__width}"
