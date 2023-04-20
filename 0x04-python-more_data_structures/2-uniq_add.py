#!/usr/bin/python3
# 2-uniq_add.py
# Brennan D Baraban <375@holbertonschool.com>


def uniq_add(my_list=[]):
    """Add all unique integers in a list (once for each integer)."""
    new_set=set(my_list)
    sum = 0
    for i in new_set:
        sum += i
    return (sum)
