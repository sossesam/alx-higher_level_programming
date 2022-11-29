#!/usr/bin/python3

def pow(a, b):
    result = 1
    i = 1
    length = b
    if b < 0:
        length = length * -1

    for i in range(length):
        if b < 0:
            result = result / a
        else:
            result = result * a

    return result
