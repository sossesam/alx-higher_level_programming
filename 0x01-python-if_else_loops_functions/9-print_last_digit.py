#!/usr/bin/python3

def print_last_digit(number):
    if number < 0:
        number = number * (-1)
        answer = number % 10

    else:
       answer = number % 10
    
    print("{}".format(answer), end="")
    return answer
