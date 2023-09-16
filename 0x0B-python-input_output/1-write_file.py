#!/usr/bin/python3

"""pass"""


def write_file(filename="", text=""):
    """pass"""
    with open(filename, "w", encoding="utf-8") as the_file:
        return the_file.write(text)
