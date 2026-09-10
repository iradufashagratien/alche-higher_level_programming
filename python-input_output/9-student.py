#!/usr/bin/python3
"""Defines a class Student."""


class Student:
    """Student class - defines a student by name and age."""

    def __init__(self, first_name, last_name, age):
        """Initialize a new Student.

        Args:
            first_name (str): the student's first name.
            last_name (str): the student's last name.
            age (int): the student's age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Return a dictionary representation of this Student instance.

        Returns:
            dict: the attribute dictionary of this Student.
        """
        return self.__dict__
