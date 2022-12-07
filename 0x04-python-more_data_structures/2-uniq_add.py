#!/usr/bin/python3

def uniq_add(my_list=[]):
    newList = []
    for x in my_list:
        if x not in newList:
            newList.append(x)

    def sum_up(test = []):
        z = 0
        for y in test:
            z = y + z
        return z

    result = sum_up(newList)

    return result
