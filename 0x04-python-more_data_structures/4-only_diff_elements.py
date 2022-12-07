#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    newList = []
    for x in set_1:
        if (x not in set_2) and x not in newList:
            newList.append(x)
    for x in set_2:
        if (x not in set_1) and x not in newList:
            newList.append(x)

    return newList