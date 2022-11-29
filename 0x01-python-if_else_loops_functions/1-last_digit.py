#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# YOUR CODE HERE
dg = number % 10

if number > 0:
    if dg > 5:
        print(f"Last digit of {number} is {dg} and is greater than 5")
    elif dg < 6:
        print(f"Last digit of {number} is {dg} and is less than 6 and not 0")
    else:
        print(f"Last digit of {number} is {dg} and is 0")

elif number < 0:
    number = number * (-1)
    dg = number % 10
    dg = dg * (-1)
    number = number * (-1)
    if dg == 0:
        print(f"Last digit of {number} is {dg} and is 0")

    else:
        print(f"Last digit of {number} is {dg} and is less than 6 and not 0")

else:
    print(f"Last digit of {number} is {dg} and is 0")
