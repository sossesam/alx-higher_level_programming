#!/usr/bin/python3

def safe_print_integer(value):
    try:
        if value + 1:
            print("{:d}".format(value))
            return True
    except:
        return False
