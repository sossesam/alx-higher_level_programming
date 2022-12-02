#!/usr/bin/python3
if __name__ == '__main__':
    import sys

argv = sys.argv[1:]
x = len(argv)
if x > 0:
    print(f"{x} arguments:")
    for i in range(x):
        print(f"{i + 1}: {argv[i]}")
else:
    print(f"{x} arguments.")


