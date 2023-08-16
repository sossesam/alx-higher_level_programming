#!/usr/bin/python3

def search_replace(my_list, search, replace):
    def find_number(x):
        if x == search:
            return replace
        else:
            return x

    return list(map(find_number, my_list))
