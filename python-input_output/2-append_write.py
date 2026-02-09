#!/usr/bin/python3
def append_write(filename="", text=""):
    """
    Appends a string at the end of a text file (UTF-8)
    and returns the number of characters added
    """

    # Open the file in append mode ("a+")
    # The file is created if it does not exist
    # The file is automatically closed after the 'with' block
    with open(filename, "a+", encoding="utf-8") as f:

        # Write the given text at the end of the file
        f.write(text)

        # Return the number of characters written
        return len(text)
