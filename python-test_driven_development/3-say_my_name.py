#!/usr/bin/python3
"""
task 3-say_my_name
Args first_name, last_name
"""


def say_my_name(first_name, last_name=""):
    """
    prints first name and last name handling errors
    >>> say_my_name("John", "Smith")
    My name is John Smith$
    >>> say_my_name("Walter", "White")
    My name is Walter White$
    >>> say_my_name("$")
    My name is $ $
    >>> say_my_name()
    Traceback (most recent call last):
    ...
    TypeError: say_my_name() missing 1 required positional argument: 'first_name'
    >>> say_my_name("Bob")
    My name is Bob $
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    else:
        print("My name is {:s} {:s}$".format(first_name, last_name))
