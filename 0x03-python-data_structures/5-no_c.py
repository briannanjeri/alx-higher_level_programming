#!/usr/bin/python3
# 5-no_c.py
# no_c


def no_c(my_string):
    """Remove all characters c and C from a string."""
    newstring = [i for i in my_string if i != 'c' and i != 'C']
    return ("".join(newstring))
