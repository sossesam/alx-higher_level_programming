#!/usr/bin/python3

if __name__ == '__main__':
    from sys import argv

x = argv[1:]
result = 0
for i in range(len(argv) - 1):
    result = result + int(x[i])
