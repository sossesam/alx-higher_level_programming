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

        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

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

    @width.getter
    def width(self):
        return self.__width

    @width.setter
    def width(self, width):
        self.__width = width

    @height.setter
    def height(self, height):
        self.__height = height


    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y
