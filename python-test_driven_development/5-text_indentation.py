#!/usr/bin/python3

def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these
    characters: ., ? and :

    Args:
        text (_type_): _description_
    Raises:
        TyperError: If text is not a string.

    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    special_chars = ['.', '?', ':']
    for char in special_chars:
        text = text.replace(char, char + '\n\n')

    lines = text.split('\n')
    for line in lines:
        print(line.strip())
