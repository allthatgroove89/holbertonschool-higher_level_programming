#!/usr/bin/python3

def islower(c):
    if c == '':
        raise ValueError("Input cannot be an empty string")
    elif "a" <= c <= "z":
        return True
    else:
        return False
