#!/usr/bin/python3
"""
A function that returns True
if the object is exactly an instance of the class
"""


def is_same_class(obj, a_class):
    """Compares object with class"""
    if type(obj) is a_class:
        return True
    else:
        return False
