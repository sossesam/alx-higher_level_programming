#!/usr/bin/python3
def print_reversed_list_integer(my_list):
    i = len(my_list) - 1
    while i >= 0 and isinstance(my_list[i], int):
        print("{:d}".format(my_list[i]))
        i -= 1
