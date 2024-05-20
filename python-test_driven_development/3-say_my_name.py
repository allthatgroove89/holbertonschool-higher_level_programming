#!/usr/bin/python3
"""
task 3-say_my_name
Args first_name, last_name
"""


def say_my_name(first_name, last_name=""):
    """
    prints first name and last name handling errors
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string$")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string$")
    else:
        print("My name is {} {}$".format(first_name, last_name))
