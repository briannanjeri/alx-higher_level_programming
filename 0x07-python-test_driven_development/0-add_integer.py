#!/usr/bin/python3
"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""


def add_integer(a, b):
    """Return the addition of two numbers."""
     if not isinstance(a, (int, float)):
      raise TypeError("a must be an integer or b must be an integer")
     elif not isinstance(b, (int, float)):
      raise TypeError("a must be an integer or b must be an integer")
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)
    return a + b
