#!/usr/bin/python3

def uppercase(str):
    for char in str:
        uppercase_char = char

        if ord(char) >= 97 and ord(char) <= 122:

            uppercase_char = chr(ord(char) - 32)
        print("{}".format(uppercase_char), end="")
    print()
