#!/usr/bin/python3
"""pass"""


class Student:
    def __init__(self, first_name, last_name, age):
        """pass"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        items = self.__dict__
        new_dict = {}

        if attrs is not None:
            for title in attrs:
                if title in items.keys():
                    new_dict[title] = items[title]
            return new_dict
        else:
            return items

    def reload_from_json(self, json):

        self.__dict__.update(json)