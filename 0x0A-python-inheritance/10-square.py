#!/usr/bin/python3
"""pass"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """pass"""
    def __init__(self, size):
        """pass"""
        self.integer_validator("size", size)
        self.__size = size
        Rectangle.__init__(self, self.__size, self.__size)

    