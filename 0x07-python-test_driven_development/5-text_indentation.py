#!/usr/bin/python3
"""
This is the "5-test_indentation" module.
The 5-text_indentation module supplies one function, text_indentation(text).
"""


def text_indentation(text):
    """Adds a 2 new line character after "." "?" ":" """
    if type(text) is not str:
        raise TypeError("text must be a string")
    count = 0
    for c in text:
        if count == 0:
            if c == ' ':
                continue
            else:
                count = 1
        if count == 1:
            if c == '?' or c == '.' or c == ':':
                print(c)
                print()
                count = 0
            else:
                print(c, end="")
