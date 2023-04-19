#!/usr/bin/python3
# 7-add_tuple.py
# Brennan D Baraban <375@holbertonschool.com>


def add_tuple(tuple_a=(), tuple_b=()):
    """Add two tuples."""
    if(len(tuple_a)<2):
        if len(tuple_a)==0:
           tuple_a=0,0
    else:
        a1,a2=tuple_a[0],tuple_a[1]
    if(len(tuple_b)<2):
        if len(tuple_a)==0:
           tuple_a=0,0
    else:
        b1,b2=tuple_b[0],tuple_b[1] 
        
    return (a1+b1, b1+b2)   
