#!/usr/bin/python3
"""square was initialized"""
class Square:
    """we initiallized the square"""
    def __init__(self,size = 0):
            if type(size) != int:
                raise TypeError("size must be an integer")
            elif size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size
    """ area- calculates the area of the square"""
    def area(self):
            size = self.__size
            return size * size


