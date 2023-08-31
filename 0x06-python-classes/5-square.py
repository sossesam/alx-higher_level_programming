#!/usr/bin/python3
"""square was initialized"""


class Square:
    """we initiallized the square"""
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    """ area - calculates the area of the square"""
    def area(self):
        size = self.__size
        return size * size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def my_print(self):
        count = self.__size

        for i in range(count):
            for y in range(count):
                print("#",end="")
            print("\n",end="")
