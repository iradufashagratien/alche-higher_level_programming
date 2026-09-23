#!/usr/bin/python3
"""Format text indentation."""


def text_indentation(text):
    """Print text with new lines after punctuation."""
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.strip()
    line = ""
    for char in text:
        if char in ".?:":
            print(line.strip() + char)
            print()
            line = ""
        else:
            line += char
    if line.strip():
        print(line.strip(), end="")
