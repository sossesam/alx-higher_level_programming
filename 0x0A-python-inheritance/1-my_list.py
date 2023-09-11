#!/usr/bin/python3

class MyList(list):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def print_sorted(self):

         print(sorted(self))

