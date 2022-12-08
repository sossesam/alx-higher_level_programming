#!/usr/bin/python3
def complex_delete(a_dictionary, values):
    delete_list = []
    for k, y in a_dictionary.items():
        if y == values:
            delete_list.append(k)

    for x in delete_list:
        a_dictionary.pop(x)
    return a_dictionary
