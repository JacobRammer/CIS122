'''
CIS 122 Fall 2018 Lab 4
Author: Jacob Rammer
Partner: None
Description: Lab 4
'''


def get_full_month(month):
    """Return the month
    Return the month to print
    Args:
        month (Int): Use month to determine what month to return

    Returns:
        month as a string
    """
    if month == 1:
        return "January"
    elif month == 2:
        return "February"
    elif month == 3:
        return "March"
    elif month == 4:
        return "April"
    elif month == 5:
        return "May"
    elif month == 6:
        return "June"
    elif month == 7:
        return "July"
    elif month == 8:
        return "August"
    elif month == 9:
        return "September"
    elif month == 10:
        return "October"
    elif month == 11:
        return "November"
    elif month == 12:
        return "December"
    else:
        return "Must be an integer between 1 and 12 (" + str(month) + " is invalid)"


def test_get_full_month():
    """Print month
    Print the month number ans month associated with it
    Returns:
        void
    """
    for i in range(14):
        if i == 1:
            print(i, "January")
        elif i == 2:
            print(i, "February")
        elif i == 3:
            print(i, "March")
        elif i == 4:
            print(i, "April")
        elif i == 5:
            print(i, "May")
        elif i == 6:
            print(i, "June")
        elif i == 7:
            print(i, "July")
        elif i == 8:
            print(i, "August")
        elif i == 9:
            print(i, "September")
        elif i == 10:
            print(i, "October")
        elif i == 11:
            print(i, "November")
        elif i == 12:
            print(i, "December")
        else:
            print(i, "Must be an integer between 1 and 12 (" + str(i) + " is invalid)")


def is_leap_year(year):
    """Test for leap year
    test to see if year is a leap year
    Args:
        year (Int): Year to test

    Returns:
        True if leap year or false if not
    """
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        return True
    else:
        return False


def test_is_leap_year(start_year, end_year):
    """Prints a bunch of leap years
    Print leap years from 1996 to 2112
    Args:
        start_year (Int): starting year
        end_year (Int): Ending year

    Returns:
        void
    """
    for i in range(start_year, end_year + 1):
        if i % 4 == 0:
            print(i)


print(get_full_month(10))
test_get_full_month()
print(is_leap_year(2020))
test_is_leap_year(1996, 2112)
