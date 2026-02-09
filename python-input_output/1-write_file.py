#!/usr/bin/python3
def write_file(filename="", text=""):
    """
    Reads a text file (UTF-8) and prints its content to stdout
    """

    with open(filename, "w+", encoding="utf-8") as f:
        f.write(text)
        return len(text)
