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

        if type(width) is int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")

        else:
            raise TypeError(f"width must be an integer")

        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")

        else:
            raise TypeError(f"height must be an integer")

        if type(x) is int:

            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError(f"x must be an integer")

        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError(f"y must be an integer")

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

    @width.setter
    def width(self, width):
        if type(width) is int:
            if width > 0:
                self.__width = width
            else:
                raise ValueError("width must be > 0")

        else:
            raise TypeError(f"width must be an integer")

    @height.setter
    def height(self, height):
        if type(height) is int:
            if height > 0:
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError(f"height must be an integer")

    @x.setter
    def x(self, x):
        if type(x) is int:
            if x >= 0:
                self.__x = x
            else:
                raise ValueError("x must be >= 0")
        else:
            raise TypeError(f"x must be an integer")

    @y.setter
    def y(self, y):
        if type(y) is int:
            if y >= 0:
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError(f"y must be an integer")

    def area(self):
        """
        This modules contains a class rectangle
        with all its methods and attributes
        definition
        """
        return self.__width * self.__height

    def display(self):
        """
        This modules contains a class rectangle
        with all its methods and attributes
        definition
        """
        print(("\n" * self.__y) + "\n".join(((" " * self.__x) +
                                             ("#" * self.__width))
                                            for a in range(self.__height)))

    def __str__(self):
        name = type(self).__name__
        id = self.id
        x = self.__x
        y = self.__y
        return f"[{name}] ({id}) {x}/{y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """
        for
        update

        """
        position = 0
        for arg in args:
            if position == 0:
                self.id = arg
            elif position == 1:
                self.__width = arg
            elif position == 2:
                self.__height = arg
            elif position == 3:
                self.__x = arg
            elif position == 4:
                self.__y = arg
            position += 1

        if "id" in kwargs:
            self.id = kwargs["id"]
        if "width" in kwargs:
            self.__width = kwargs["width"]
        if "height" in kwargs:
            self.__height = kwargs["height"]
        if "x" in kwargs:
            self.__x = kwargs["x"]
        if "y" in kwargs:
            self.__y = kwargs["y"]

    def to_dictionary(self):
        dict = {}
        dict['x'] = self.__x
        dict['y'] = self.__y
        dict["width"] = self.__width
        dict["height"] = self.__height
        dict["id"] = self.id

        return dict
