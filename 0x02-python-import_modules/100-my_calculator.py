#!/usr/bin/python3
if __name__ == '__main__':
    from calculator_1 import div, mul, add, sub
    from sys import argv

arg_len = len(argv)
operator = ['+', '-', '*', '/']
result = 0

if arg_len != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)
else:
    if argv[2] == operator[0]:
       result = add(int(argv[1]), int(argv[3]))
    elif argv[2] == operator[1]:
        result = sub(int(argv[1]), int(argv[3]))
    elif argv[2] == operator[2]:
        result = mul(int(argv[1]), int(argv[3]))
    elif argv[2] == operator[3]:
        result = div(int(argv[1]), int(argv[3]))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

print(f"{argv[1]} {argv[2]} {argv[3]} = {result}")