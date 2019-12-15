"""
CIS 122 Fall 2018 Assignment 7
Author: Jacob I Rammer
Credits: N/A
Description: List manipulation
"""

t = []  # t as an empty list


def cmd_help():
    """Display help information
    print help information from list
    :return: void
    """
    print("*** Available commands ***")

    help_command = ["Add", "Delete", "List", "Clear"]  # Commands that can be entered
    get_max_list_item_size(help_command)  # per assignment instructions. Does not seem to provide any function

    help_command_desc = ["Add to a list", "Delete information", "List information",
                         "Clear list"]  # descriptions of commands

    for item, desc in zip(help_command, help_command_desc):  # combine range to two list
        pad_left(item), pad_right(desc)

    pad_left("Empty to exit\n")


def cmd_add(t):
    """if add command
    prompts the user for items to add to list. break when empty
    :param t: item to add to list
    :return: void
    """
    while True:
        add_item = input("Enter information (empty to stop): ")
        if len(add_item) == 0:
            break
        else:
            t.append(add_item)
            print("Added, item count = " + str(len(t)))


def cmd_delete(t):
    while len(t) >= 1:
        for i in t:
            # Print the index number and item in list. Pad the string length of t by calling function
            pad_left(str(t.index(i)), 8), pad_right(str(i), 2)  # number is pad space
        delete = input("\nEnter a number to delete (empty to stop): ").strip()

        if delete.isdigit():  # tests to see if input is integer
            t.pop(int(delete))  # delete element

        elif len(delete) == 0:
            break
        else:
            print("Unknown command")
    print("All items deleted")  # print only when list is empty


def cmd_list(t):
    """display the contents of list
    :param t: list
    :return: void
    """
    print("List contains " + str(len(t)) + " item(s)")
    for item in t:
        print(item)


def cmd_clear(t):
    """clear the list
    :param t: list
    :return: void
    """
    length = len(t)  # get the length of the list before it's cleared
    t.clear()
    print(str(length) + " item(s) removed, list empty")


def get_max_list_item_size(t):
    """
    Get the length of t
    :param t: list
    :return: length of t
    """
    return len(t)


def pad_left(string, space=10):  # Pads the string to the leftmost position
    """Pads left
    Pads the string to the left of the console
    :param string: String to be formatted
    :param space: Inserts space to format
    :return: Void
    """
    print(string.ljust(space), end="")


def pad_right(string, space=10):  # Prints the string to the rightmost position
    """Pads left
    Pads the string to the left of the console without a newline at the end
    :param string: String to be formatted
    :param space: Inserts space to format
    :return: Void
        """
    print(string.rjust(space))


while True:
    command = input("Enter a command (? for help): ").strip().lower()
    if len(command) == 0:
        break
    else:
        if command == "?":
            cmd_help()
        elif command == "add":
            cmd_add(t)
        elif command == "del":
            cmd_delete(t)
        elif command == "list":
            cmd_list(t)
        elif command == "clear":
            cmd_clear(t)
        else:
            print("Unknown command")
