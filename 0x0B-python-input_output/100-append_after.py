#!/usr/bin/python3

def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line
    containing a specific string.

    Args:
        filename (str): Name of the file.
        search_string (str): String to search for in each line.
        new_string (str): String to append after lines containing
        the search string.

    Returns:
        None
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)


if __name__ == "__main__":
    import sys

    filename = sys.argv[1]
    search_string = sys.argv[2]
    new_string = sys.argv[3]
    append_after(filename, search_string, new_string)
