#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for text in my_string:
        if text != 'c' and text != 'C':
            new_string += text

    return new_string
