#!/usr/bin/python3

def print_last_digit(number):
    number = abs(number)
    last_digit = number % 10
    print("{:d}".format(last_digit), end="")
    return last_digit
