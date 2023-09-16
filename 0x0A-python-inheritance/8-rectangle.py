#!/usr/bin/python3
"""pass"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry



class Rectangle(BaseGeometry):
    """pass"""
    def __init__(self, width, height):
        """pass"""
        if self.integer_validator("width", width):
            self.__width = width
        if self.integer_validator("height", width):
            self.__height = height
