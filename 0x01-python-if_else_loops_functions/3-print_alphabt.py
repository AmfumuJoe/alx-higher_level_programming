#!/usr/bin/python3

for a in range(ord('a'), ord('z') + 1):
    if chr(a) == 'e' or chr(a) == 'q':
        continue
    else:
        print("{:c}".format(a), end='')
