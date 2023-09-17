#!/usr/bin/python3

"""pass"""

import json
def load_from_json_file(filename):
    """pass"""
    with open(filename, "r") as object:
        data = json.load(object)
    return data
