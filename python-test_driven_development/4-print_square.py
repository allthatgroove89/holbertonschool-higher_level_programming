#!/usr/bin/python3
"""
print_square
args size
"""


def print_square(size):
    """>>> print_square(1)
    #
    >>> print_square(4)
    ####
    ####
    ####
    ####
    >>> print_square(10)
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    ##########
    #########
    ##########
    ##########
    >>> try:
    ...     print_square(None)
    ... except TypeError as e:
    ...     print(e)
    ...
    size must be an integer
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for _ in range(size):
        print("#" * size)
