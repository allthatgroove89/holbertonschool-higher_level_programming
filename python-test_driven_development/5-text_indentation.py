#!/usr/bin/python3
""" Task 4"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these
    characters: ., ? and :
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    text = text.strip()
    for i in text:
        if i not in ['.', '?', ':']:
            print(i, end="")
        else:
            print(i)
            print('\n')
