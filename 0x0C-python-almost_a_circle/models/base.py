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

    def from_json_string(json_string):
        """
        This function returns the list
        of the json string represenation
        """
        if json_string is None or len(json_string) == 0:
            return ([])
        return (json.loads(json_string))
