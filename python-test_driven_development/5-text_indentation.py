#!/usr/bin/python3
"""Print text with two new lines after ., ? and : characters.
"""


def text_indentation(text):
    """Print text while separating sentences with two new lines."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        if char in ".?:":
            print(line.strip())
            print()
            line = ""
        else:
            line += char

    if line:
        print(line.strip(), end="")
