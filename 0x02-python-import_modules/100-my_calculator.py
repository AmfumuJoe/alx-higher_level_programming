#!/usr/bin/python3
if __name__ != "__main__":
    exit(1)
from sys import argv
from calculator_1 import add, sub, mul, div
argc = len(argv)
if argc != 4:
    print("Usage: ./100-my_calculator.py <a> <operator> <b>")
    exit(1)

a = int(argv[1])
b = int(argv[3])
sign = ["+", "-", "*", "/"]

for j in enumerate(sign):
    if argv[2] == sign[0]:
        result = add(a, b)
        break
    elif argv[2] == sign[1]:
        result = sub(a, b)
        break
    elif argv[2] == sign[2]:
        result = mul(a, b)
        break
    elif argv[2] == sign[3]:
        result = div(a, b)
        break
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)
print("{:d} {:s} {:d} = {:d}".format(a, argv[2], b, result))
