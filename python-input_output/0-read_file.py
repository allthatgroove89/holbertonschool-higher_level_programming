#!/usr/bin/python3
"""This module contains a function that reads
a file and prints its content to stdout.
"""


def read_file(filename=""):
    """Reads a file and prints its content to stdout.
    """
    with open(filename, 'r', encoding="utf-8") as file:
        print(file.read(), end="")
