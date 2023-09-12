#!/usr/bin/python3
"""takes a list class and returns it in a sorted format"""


class MyList(list):
    """the initialisation process"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    """method to sort the list"""
    def print_sorted(self):

         print(sorted(self))

