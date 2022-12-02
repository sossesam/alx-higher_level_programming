#!/usr/bin/python3
if __name__ == '__main__':
    from sys import argv

n = len(argv) - 1
if n > 0:
    print(f"{n} arguments:")
    for i in range(n):
        print(f"{i + 1}: {argv[i + 1]}")
else:
    print(f"{n} arguments.")
