#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    """Locked class that restricts attributes"""

    def __setattr__(self, name, value):
        """Only allow first_name attribute"""
        if name != 'first_name':
            raise AttributeError(
                "'LockedClass' object has no attribute '{}'".format(name)
            )
        object.__setattr__(self, name, value)
