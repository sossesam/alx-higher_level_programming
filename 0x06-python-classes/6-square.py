#!/usr/bin/python3
"""square was initialized"""


class Square:
    """we initiallized the square"""
    def __init__(self, size=0, position=(0, 0)):
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

        if type(position) != tuple:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(position) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif type(position[0]) is not int or type(position[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = position

    """ area - calculates the area of the square"""
    def area(self):
        size = self.__size
        return size * size

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        self.__position = value

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        self.__size = value

    def my_print(self):
        count = self.__size
        position = self.__position

        if count <= 0:
            print()
            return
        else:
            for a in range(self.position[1]):
                print()
            for a in range(self.size):
                print("{}{}".format(" " * self.position[0], "#" * self.size))
