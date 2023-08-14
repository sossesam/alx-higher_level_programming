#!/usr/bin/python3
def print_reversed_list_integer(my_list):
    i = 0
    for x in my_list:
        i += 1
    x-=1
    while x >= 0:
        print("{:d}".format(my_list[x]))
        x-=1
