#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first_name> <last_name>".
    Parameters:
    first_name (str): The first name of the person.
    last_name (str, optional): The last name of the person.\
          Defaults to an empty string.
    Raises:
    TypeError: If either `first_name` or `last_name` is not a string.
    Example:
    >>> say_my_name("John", "Smith")
    My name is John Smith
    >>> say_my_name("Walter")
    My name is Walter
    >>> say_my_name(12, "White")
    Traceback (most recent call last):
        ...
    TypeError: first_name must be a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}".strip())
