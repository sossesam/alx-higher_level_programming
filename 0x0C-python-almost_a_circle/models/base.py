#!/usr/bin/python3
"""
This modules contains a class Base
with all its methods and attributes
definition
"""

import json


class Base():
    """
    This class has a private attribute __nb_objects = 0
    a class constructor definition to check for id
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Instantiation of class which checks for id
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        This functions returns the json string representation
        of list_dictionaries
        """
        if list_dictionaries is None:
            list_dictionaries = []
        return (json.dumps(list_dictionaries))
