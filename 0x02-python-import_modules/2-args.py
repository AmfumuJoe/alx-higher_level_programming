#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    i = 0
    argc = len(argv) - 1
    string = "argument"
    if argc > 1:
        string += 's:'
    elif argc == 0:
        string += "s."
    elif argc == 1:
        string += ":"
    print("{:d} {:s}".format(argc, string))
    for arguments in argv:
        if i != 0:
            print("{:d}: {:s}".format(i, arguments))
        i += 1
