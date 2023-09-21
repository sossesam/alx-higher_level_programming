#!/usr/bin/python3
"""
This modules contains a class rectangle
with all its methods and attributes
definition
"""

from models.base import Base


class Rectangle(Base):
    """
    This modules contains a class rectangle
    with all its methods and attributes
    definition
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        This modules contains a class rectangle
        with all its methods and attributes
        definition
        """
        Base.__init__(self, id)

        if type(width) is int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")

        else:
            raise TypeError(f"width must be an integer")

        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")

        else:
            raise TypeError(f"height must be an integer")

        if type(x) is int:

            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be > 0")
        else:
            raise TypeError(f"x must be an integer")

        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be > 0")
        else:
            raise TypeError(f"y must be an integer")

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @width.setter
    def width(self, width):
        if type(width) is int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")

        else:
            raise TypeError(f"width must be an integer")

    @height.setter
    def height(self, height):
        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError(f"height must be an integer")

    @x.setter
    def x(self, x):
        if type(x) is int:
            self.__x = x
        else:
            raise TypeError(f"x must be an integer")

    @y.setter
    def y(self, y):
        if type(y) is int:
            self.__y = y
        else:
            raise TypeError(f"height must be an integer")
