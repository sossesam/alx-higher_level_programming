#!/usr/bin/python3
""" This module find the highest number """

def find_peak(number):
    """this the the function"""
    pos = 0
    maxiim = 0
    if len(number) == 0:
        return None

    if len(number) % 2 == 0:
        max1 = 0
        while pos < len(number) - 1:
            
            if number[pos] >  number[pos + 1]:
                max1 = number[pos]
            else:
                max1 = number[pos + 1]
            
            if maxiim < max1:
                maxiim = max1

            pos = pos + 2
    else:
        max1 = 0

        if number[pos] >  number[pos + 1]:
                max1 = number[pos]
        pos = pos + 1
        
        while pos < len(number) - 1:
            
            if number[pos] >  number[pos + 1]:
                max1 = number[pos]
            
            else:
                max1 = number[pos + 1]
            
            if maxiim < max1:
                maxiim = max1

            pos = pos + 2


    return maxiim




