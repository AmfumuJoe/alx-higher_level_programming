#!/usr/bin/python3
"""

a function that adds 2 integers

Prototype: def add_integer(a, b=98):
a and b must be integers or floats, otherwise raise
a TypeError exception with the message a must be an integer or b must be an integer
a and b must be first cast to integers if they are float
Returns an integer: the addition of a and b

"""


def add_integer(a, b=98):
    """Return the sum of two integers or floats as integers

    Args:
        a: first argument
        b: second argument

    Returns:
        Sum of the two arguments

    Raises:
        TypeError: If either of the arguments not an integer or a float
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
