#!/usr/bin/python3
"""
Module to check if an object is an instance
of a class that inherited from a specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a
    class that inherited from a specified class.
    """
    if isinstance(obj, a_class) and type(obj) is not a_class:
        """Returns:
        True if 'obj' is an instance,
        False otherwise."""
        return True
    else:
        return False
