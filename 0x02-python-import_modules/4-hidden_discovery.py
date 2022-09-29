#!/usr/bin/python3
if __name__ != "__main__":
    exit(0)
import hidden_4 as hidden
for name in dir(hidden):
    if name[0:2] == '__':
        continue
    print(name)
