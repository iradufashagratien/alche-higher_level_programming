#!/usr/bin/python3
"""LockedClass module"""


class LockedClass:
    """Locked class restricts attributes"""

    def __setattr__(self, name, value):
        if name != 'first_name':
            msg = "'LockedClass' object has no attribute '" + name + "'"
            raise AttributeError(msg)
        object.__setattr__(self, name, value)
