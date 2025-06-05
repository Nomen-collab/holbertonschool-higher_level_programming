#!/usr/bin/python3

"""
This module provides a function that appends a string to a text file
and returns the number of characters added.

Functions:
    append_write(filename="", text=""): Appends a string to a text file
    and returns the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file and returns the number of characters added.

    Args:
        filename (str): The name of the file to append to. Defaults to an empty
        string.
        text (str): The string to append to the file. Defaults to an empty
        string.

    Returns:
        int: The number of characters added to the file.
    """
    with open(filename, 'a', encoding="utf-8") as file:
        num_chars_appended = file.write(text)
        return num_chars_appended
