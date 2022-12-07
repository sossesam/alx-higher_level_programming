#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    b_dictionary = {}

    a_list = []
    for x in a_dictionary.keys():
        a_list.append(x)

    new_list = sorted(a_list)
    for x in new_list:
        b_dictionary[x] = a_dictionary[x]

    for y, x in b_dictionary.items():
        print("{}: {}".format(y, x))
