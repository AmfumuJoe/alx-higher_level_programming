#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """
prints the reverse of a given list
    """
    if type(my_list) != list:
        exit(1)
    my_list.reverse()
    for s in my_list:
        print("{:d}".format(s))
