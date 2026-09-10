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

    def to_json(self, attrs=None):
        """Return a dictionary representation of this Student instance.

        Args:
            attrs (list): optional list of attribute names to filter on.
                If provided, only matching attributes are included.
                Otherwise, every attribute is included.

        Returns:
            dict: the (optionally filtered) attribute dictionary.
        """
        if attrs is not None and isinstance(attrs, list):
            return {
                key: value for key, value in self.__dict__.items()
                if key in attrs
            }
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of this Student from a dictionary.

        Args:
            json (dict): a dictionary of attribute names to values.
        """
        for key, value in json.items():
            setattr(self, key, value)
