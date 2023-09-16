#!/usr/bin/python3
"""pass"""


def inherits_from(obj, a_class):
    """is_same_class: pass"""
    return issubclass(type(obj), a_class) and type(obj) != a_class
