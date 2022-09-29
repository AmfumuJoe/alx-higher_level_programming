#!/usr/bin/python3
from sys import argv
if __name__ != "__main__":
    exit(0)
result = 0
i = 0
for num in argv:
    if i != 0:
        result += int(num)
    else:
        i += 1
print("{:d}".format(result))
