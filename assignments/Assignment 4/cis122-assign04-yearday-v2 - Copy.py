'''
CIS 122 Fall 2018 Assignment 4
Author: Jacob Rammer
Partner: None
Description: Assignment 4 version 1
'''


def is_leap_year():  # Check assignment if I need to validate year input as well
    """Test to see if a year is a leap year
        Check to see if a year is a leap year and return true or false based
        upon the result
    :param year: (Int) Year used when calling function
    :return: True of False
    """
    year = int(input("Enter year: "))
    day = int(input("Enter day of year: "))
    month = ""
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                pass
            # If the year is a leap year
        if day <= 0:
            print("Day of year must be > 0")
            exit()
        elif day > 366:
            print("Day must be <= 366")
            exit()
        elif (day == 1) or (day <= 31):
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

    else:  # Not a leap year
        if day <= 0:
            print("Day of year must be > 0")
            exit()
        elif day > 365:
            print("Day must be <= 365")
            exit()
        elif (day == 1) or (day <= 31):
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

is_leap_year()