#!/usr/bin/python3

"""
This module defines a Student class with attributes for
first name, last name, and age,
and a method to retrieve a dictionary representation of
the instance for JSON serialization.

Classes:
    Student: Defines a student with first name, last name, and age attributes.
"""


class Student:
    """
    A class used to represent a Student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the Student instance with first name, last name, and age.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of the Student instance.

        Returns:
            dict: A dictionary containing the instance's attributes.
        """
        return self.__dict__
