#!/usr/bin/python3
"""This module contains a function that writes
a string to a text file and returns the number of
characters writen
"""


def write_file(filename="", text=""):
    """Writes a string and returns the len
    """
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)
    return len(text)
