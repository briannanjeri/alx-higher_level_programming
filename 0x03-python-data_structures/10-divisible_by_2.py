#!/usr/bin/python3
# 10-divisible_by_2.py
# Brennan D Baraban <375@holbertonschool.com>


def divisible_by_2(my_list=[]):
    """Find all multiples of 2 in a list."""
    newlist = []
    for i in range(len(my_list)):
        if my_list[i] % 2 == 0:
            newlist.append(True)
        else:
            newlist.append(False)

    return (newlist)
