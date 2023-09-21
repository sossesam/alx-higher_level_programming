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
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

        Base.__init__(self, id)
