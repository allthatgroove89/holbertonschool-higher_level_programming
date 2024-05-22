#!/usr/bin/python3
"""
Check if an object is an instance or inherited from a specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an object is an instance or inherited from a specified class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False
