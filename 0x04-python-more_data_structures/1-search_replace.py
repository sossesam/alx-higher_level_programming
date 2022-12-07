#!/usr/bin/python3

def search_replace(my_list, search, replace):
        newNumber = lambda x :  replace if(x == search) else x
        return list(map(newNumber, my_list))
