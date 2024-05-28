#!/usr/bin/python3
"""
This module contains a function that appends
a string to a text file and returns the number of
characters added
"""


def append_write(filename="", text=""):
    """Appends a string to text file
    and returns len
    """
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
