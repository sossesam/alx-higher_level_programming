#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    x = []

    for i in range(len(my_list)):
        if i % 2 == 0 and i > 1:
            x.append(True)
        else:
            x.append(False)
    return x
