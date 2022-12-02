#!/usr/bin/python3

import sys

n = len(sys.argv) - 1
x = (sys.argv)
if n > 0:
    print(f"{n} arguments:")
    for i in range(n):
        print(f"{i + 1}: {x[i + 1]}")      
else:
    print(f"{n} arguments.")