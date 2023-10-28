#!/usr/bin/python3

""" the module contains various function for calculations"""


def add_integer(a, b=98):
    """
    >>> add_integer(1, 2)
    3

    >>> add_integer("1", 2)
    Traceback (most recent call last):
        ...
    TypeError: a must be an integer

    >>> add_integer(2, "1")
    Traceback (most recent call last):
    ...
    TypeError: b must be an integer

    >>> add_integer(100, -2)
    98

    >>> add_integer(2)
    100

    >>> add_integer(100.3, -2)
    98
    """

    if type(a) != int  and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    elif type(a) == float:
        a = int(a)
    elif type(b) == float:
        b = int(b)
    return a + b


