#!/usr/bin/python3
# 8-uppercase.py

def uppercase(s):
    """Print a string in uppercase followed by a new line."""
    for char in s:
        if ord(char) >= 97 and ord(char) <= 122:
            uppercase_char = chr(ord(char) - 32)
        else:
            uppercase_char = char
        print("{}".format(uppercase_char), end="")
    print()
