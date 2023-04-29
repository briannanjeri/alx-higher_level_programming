#!/usr/bin/python3
# 9-max_integer.py
# nanjeribrian


def max_integer(my_list=[]):
    """Find the biggest integer of a list."""
    if not my_list:
        return (None)

    max = my_list[0]
    for i in range(len(my_list)):
        if my_list[i] > max:
            max = my_list[i]

    return (max)
