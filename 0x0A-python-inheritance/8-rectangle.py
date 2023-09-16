#!/usr/bin/python3
"""pass"""


class BaseGeometry:
    """pass"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates value"""
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))

class Rectangle(BaseGeometry):
    """pass"""
    def __init__(self, width, height):
        """pass"""
        if self.integer_validator(self, width):
            self.__width = width
        if self.integer_validator(self, width):
            self.__height = height
