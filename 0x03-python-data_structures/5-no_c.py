#!/usr/bin/python3
def no_c(my_string):
    """
        a function that removes all characters c and C from a string.
    """
    new_string = ""
    if type(my_string) == str:
        for s in my_string:
            if s not in 'cC':
                new_string += s
        return (new_string)
