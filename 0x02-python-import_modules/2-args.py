#!/usr/bin/python3

import sys

n = len(sys.argv) - 1
argv = sys.argv
if n > 0:
    print(f"{n} arguments:")
    for i in range(n):
        print(f"{i}: {argv[i + 1]}")      
else:
    print(f"{n} arguments.")
       


            



