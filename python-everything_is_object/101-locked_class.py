#!/usr/bin/python3
"""Module for LockedClass"""


class LockedClass:
    """Class that only allows first_name attribute"""

    def __setattr__(self, name, value):
        """Restrict attribute assignment to first_name only"""
        if name == 'first_name':
            self.__dict__[name] = value
        else:
            raise AttributeError(f"'LockedClass' object has no attribute '{name}'")
