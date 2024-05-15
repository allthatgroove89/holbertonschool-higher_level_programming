#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    j = 0
    for value in my_list:
        if i == x:
            break
        try:
            print("{:d}".format(value), end="")
            i += 1
        except (TypeError, ValueError):
            pass
    print()
    j += 1
    if x > i:
        raise IndexError("list index out of range")
    return i
