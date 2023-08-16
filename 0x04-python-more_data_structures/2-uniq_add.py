#!/usr/bin/python3

def uniq_add(my_list=[]):
    newList = []
    for x in my_list:
        if x not in newList:
            newList.append(x)

    def sum_up(paramList=[]):
        z = 0
        for y in paramList:
            z = y + z
        return z

    result = sum_up(newList)

    return result
