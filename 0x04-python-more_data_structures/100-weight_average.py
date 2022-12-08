#!/usr/bin/python3
def weight_average(my_list=[]):
    def mul(x):
        return x[0] * x[1]

    if len(my_list) > 0:
        for x in my_list:
            add = sum(list(map(mul, my_list)))
            div = sum(list(map(lambda x: x[1], my_list)))
            result = add/div
        return result
    else:
        return 0
