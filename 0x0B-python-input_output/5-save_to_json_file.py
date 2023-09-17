#!/usr/bin/python3
"""pass"""


import json



def save_to_json_file(my_obj, filename):
    """pass"""
    with open(filename, "w") as file:
        obj = json.dumps(my_obj)
        return file.write(obj)
