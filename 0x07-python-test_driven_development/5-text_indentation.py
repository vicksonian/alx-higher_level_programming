#!/usr/bin/python3
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':'

    Args:
        text (str): The input text.

    Raises:
        TypeError: If the input is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    separator = False
    for char in text:
        if char in '.?:':
            print(char)
            print()
            separator = True
        elif separator and char == ' ':
            pass
        else:
            print(char, end='')
            separator = False
