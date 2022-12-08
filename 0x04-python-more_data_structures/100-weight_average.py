#!/usr/bin/python3
my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
def weight_average(my_list=[]):
    def mul(x):
        return x[0] * x[1]


    if len(my_list) > 0:
        for x in my_list:
         result =  round(sum(list(map(mul,my_list))), 2)/round(sum(list(map(lambda x: x[1], my_list))), 2)
         

    print(result)

weight_average(my_list)