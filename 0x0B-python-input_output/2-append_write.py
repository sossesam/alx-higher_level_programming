#!/usr/bin/python3

"""pass"""


def append_write(filename="", text=""):
    """pass"""
    with open(filename, "a", encoding="utf-8") as the_file:
        return the_file.write(text)
