#!/usr/bin/python3
def print_reversed_list_integer(my_list):
    i = 0
    for x in my_list:
        i += 1


    i-=1
    while i >= 0:
        print("{:d}".format(my_list[i]))
        i-=1



