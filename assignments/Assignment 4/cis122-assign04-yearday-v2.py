'''
CIS 122 Fall 2018 Assignment 4
Author: Jacob Rammer
Partner: None
Description: Assignment 4 version 2
'''


def is_leap_year(year):
    """Determine is inputted year is a leap year
Tests if year is a leap year
    Args:
        year (Int): information to test

    Returns:
        True if true or False if false
    """

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
        return True
    else:
        return False


def valid_year(year):
    """Validates year
    validates that year is greater than 0. If not, prints error message
    Args:
        year (Int): year that is being tested

    Returns:
        True if year is greater than 0. False for all other situations
    """
    if year > 0:
        return True
    else:
        print("Year must be > 0")
        return False


def valid_day_of_year(year, day_of_year):
    """validates that the day of the year is valid
    validates that day of the year is greater than 0
    Args:
        year (Int): Not used. Just coded since it was included in instructions
        day_of_year (Int): number to be tested to see if it's greater than 0

    Returns:
        True if day_of_year is greater than 0. False for all other situations
    """
    if day_of_year > 0:
        return True
    else:
        print("Day of year must be > 0")
        return False


def input_year():
    """Input the year
    Prompt the user to input the year
    Returns:
    year as an integer. Else 0 if year is not valid
    """
    year = int(input("Enter year: "))
    while year <= 0:
        print("Day of year must be > 0")
        year = int(input("Enter year: "))
    if valid_year(year) is True:
        return year


def get_days_in_year(year):
    """Get number of days in year
    Get the day of the year depending on if year is a leap year or not
    Args:
        year (Int): Year to be tested for leap year status

    Returns:
        Day of year as an integer. 0 for unknown situations
    """
    if is_leap_year(year) is True:
        return 366
    if is_leap_year(year) is False:
        return 365
    else:
        return 0


def input_day_of_year(year):
    """input the day of the year
    Prompt the user to input year and validate input
    Args:
        year (Int): Uses the year from input_year to determine if day inputted is valid

    Returns:
        day as an integer, or 0 if input is invalid
    """
    day = int(input("Enter day of year: "))
    if is_leap_year(year) is True:
        while day > get_days_in_year(year) or day <= 0:
            while day > get_days_in_year(year):
                print("Day must be <= 366")
                day = int(input("Enter day of year: "))
            while day <= 0:
                print("Day must be > 0")
                day = int(input("Enter day of year: "))
        if valid_year(year) and valid_day_of_year(year, day) and day <= get_days_in_year(year):
            return day
    elif is_leap_year(year) is False:
        while day > get_days_in_year(year) or day <= 0:
            while day > get_days_in_year(year):
                print("Day must be <= 365")
                day = int(input("Enter day of year: "))
            while day <= 0:
                print("Day must be > 0")
                day = int(input("Enter day of year: "))
        if valid_year(year) and valid_day_of_year(year, day) and day <= get_days_in_year(year):
            return day
        else:
            return 0


def valid_month(month):
    """Determines if month is valid
    Not used. Nut function determine if month value is between 1 and 12
    Args:
        month (Int): Month to test

    Returns:
        True if month is valid, False if month is not valid
    """
    if 0 < month <= 12:
        return True
    elif month <= 0:
        print("Month must be > 0")
        return False
    elif month >= 12:
        print("Month must be <= 12")
        return False


def translate_month(month):
    """Translate the month
    Not used. But will translate month depending on the inputted value
    Args:
        month (Str): Associate month with correct month string

    Returns:
        Month as a string
    """
    if valid_month(month) is True:
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
        return ''


def get_days_in_month(year, month):
    """Get days in a month based on input
    Not used. Will return the days in each month based if the date is a leap year or not
    Args:
        year (Int): Will test if year is a leap year ot not
        month (Int): Tests the value of each month

    Returns:
        Day of month as an integer
    """
    if month == 1:
        return 31
    elif is_leap_year(year) is True and valid_month(month) is True and month == 2:  # If it's a leap year
        return 29
    elif is_leap_year(year) is False and valid_month(month) is True and month == 2:  # If it's not a leap year
        return 28
    elif month == 3:
        return 31
    elif month == 4:
        return 30
    elif month == 5:
        return 31
    elif month == 6:
        return 30
    elif month == 7:
        return 31
    elif month == 8:
        return 31
    elif month == 9:
        return 30
    elif month == 10:
        return 31
    elif month == 11:
        return 30
    elif month == 12:
        return 31
    else:
        return 0


def valid_day(year, month, day):
    """Determine if the date string is valid
    Test to see if valid_year, valid_month, and valid_day_of_year is True
    Args:
        year (Int): Year to test id valid
        month (Int): Month to test if valid
        day (Int): Day to test if valid

    Returns:
        True if true, False if false
    """
    if valid_year(year) is True and valid_month(month) is True and valid_day_of_year(year, day) is True:
        return True
    else:
        return False


def get_date_string(year, month, day):
    """Print the date
    Print the date as a string based upon user input. Tests user input to see what the string is
    Args:
        year (Int): Year to print in string
        month (Str): Month to print in string
        day (Int): Day to print in string

    Returns:
        void
    """
    if is_leap_year(year) is True and valid_year(year) is True:
        if (day == 1) or (day <= 31):
            month = "January"
        elif (day == 32) or (day <= 60):
            month = "February"
            day = day - 31
        elif (day == 61) or (day <= 91):
            month = "March"
            day = day - 60
        elif (day == 92) or (day <= 121):
            month = "April"
            day = day - 91
        elif (day == 122) or (day <= 152):
            month = "May"
            day = day - 121
        elif (day == 153) or (day <= 182):
            month = "June"
            day = day - 152
        elif (day == 183) or (day <= 213):
            month = "July"
            day = day - 182
        elif (day == 214) or (day <= 244):
            month = "August"
            day = day - 213
        elif (day == 245) or (day <= 274):
            month = "September"
            day = day - 244
        elif (day == 275) or (day <= 305):
            month = "October"
            day = day - 274
        elif (day == 306) or (day <= 335):
            month = "November"
            day = day - 305
        elif (day == 336) or (day <= 366):
            month = "December"
            day = day - 335
        print(month, str(day) + ",", year)
    if is_leap_year(year) is False and valid_year(year) is True:
        if (day == 1) or (day <= 31):
            month = "January"
        elif (day == 32) or (day <= 59):
            month = "February"
            day = day - 31
        elif (day == 60) or (day <= 90):
            month = "March"
            day = day - 59
        elif (day == 91) or (day <= 120):
            month = "April"
            day = day - 90
        elif (day == 121) or (day <= 151):
            month = "May"
            day = day - 120
        elif (day == 152) or (day <= 181):
            month = "June"
            day = day - 151
        elif (day == 182) or (day <= 212):
            month = "July"
            day = day - 181
        elif (day == 213) or (day <= 243):
            month = "August"
            day = day - 212
        elif (day == 244) or (day <= 273):
            month = "September"
            day = day - 243
        elif (day == 274) or (day <= 304):
            month = "October"
            day = day - 273
        elif (day == 305) or (day <= 334):
            month = "November"
            day = day - 304
        elif (day == 335) or (day <= 365):
            month = "December"
            day = day - 334
        print(month, str(day) + ",", year)


def start():
    """Brings together all functions
    Calls all functions needed to complete program
    Returns:
        Void
    """
    month = get_date_string
    year = input_year()
    get_date_string(year, month, input_day_of_year(year))


start()
# valid_day(2020, 2, 20)
# print(input_day_of_year(input_year()))
# input_year()
# print(valid_day_of_year(2020, 2020))
