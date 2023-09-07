#!/usr/bin/python3

"""0-square defines a squar"""


class Rectangle:
    """instantiate class"""
    def __init__(self, width=0, height=0):
        """Define width"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        """Define height"""
        if type(height) is not int:
            raise TypeError("width must be an integer")
        elif height < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(self.__width) is not int:
            raise TypeError("width must be an integer")
        if self.__width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value



    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(self.__height) is not int:
            raise TypeError("width must be an integer")
        if self.__height < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__height = value


