#!/usr/bin/python3

"""0-square defines a squar"""


class Rectangle:
    """instantiate class"""
    def __init__(self, width=0, height=0):
        """Define width"""
        if type(width) != int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = width

        """Define height"""
        if type(height) != int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        area = self.__height * self.__width
        return area

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            perimeter = (2 * self.__height) + (2 * self.__width)
            return perimeter

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ""

        else:
            height = self.__height
            while height + 1 > 2:
                print("#" * self.__width)
                height = height - 1
            return "#" * self.__width


    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")
