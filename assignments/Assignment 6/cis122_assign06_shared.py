'''
CIS 122 Fall 2018 Assignment 6
Author: Jacob Rammer
Partner: None
Description: Python Shared Code Module
'''


def pad_string(string, space):
    """Does nothing at the moment
    Longer description
    :param string (STR): String to be formatted
    :param space (CHR): Inserts space to format
    :return: Void
    """
    print(string.ljust(space))


def pad_left(string, space):  # Pads the string to the leftmost position
    """Pads left
    Pads the string to the left of the console
    :param string (STR): String to be formatted
    :param space (CHR): Inserts space to format
    :return: Void
    """
    print(string.rjust(space))


def pad_right(string, space):  # Prints the string to the rightmost position
    """Pads left
    Pads the string to the left of the console without a newline at the end
    :param string (STR): String to be formatted
    :param space (CHR): Inserts space to format
    :return: Void
        """
    print(string.ljust(space), end="")

