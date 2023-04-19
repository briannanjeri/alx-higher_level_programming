#!/usr/bin/python3
# 4-new_in_list.py
# Brennan D Baraban <375@holbertonschool.com>


def new_in_list(my_list, idx, element):
    """Replace an element in a copied list at a specific position."""
    if idx < 0 or idx > (len(my_list) - 1):
        return (my_list)
    new_list=[]
    for i in range(len(my_list)):
        new_list.append(my_list[i])
    new_list[idx]=element
    return new_list
