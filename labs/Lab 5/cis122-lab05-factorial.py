'''
CIS 122 Fall 2018 Lab 5
Author: Jacob I Rammer
Credit: None
Description: Calculate factorials
'''


import math


def factorial(num):
    """Print factorial
    Accept an integer to factorial
    Args:
        num (Int): Number to factorial

    Returns:
        Total
    """
    # Determine if num is less than 0. Return error
    # If the number is 0, return 1
    # If number is valid, set total to 1 and multiply by loop value

    total = int(1)
    if not isinstance(num, int) and not isinstance(num, float):
        print("Unexpected value")
        return
    if num < 0:
        print("Must be >= 0")
        return
    if num == 0:
        return 1
    else:
        for i in range(int(num)):
            total = total * (i + 1)
            #  print(total)
        print(total)
        return total


num = int(input("Enter factorial number: "))
factorial(num)


def test_factorial(num):
    """Test to see if factorials ==
    test to see if my factorial is equal to math.factorial

    Args:
        num (Int): Number to factorial

    Returns:
        void
    """
    total = int(1)
    factorial_num = int(1)
    errors = 0
    range_num = num + 1
    my_result = factorial(num)
    factorial_result = math.factorial(num)
    print("*" + str(my_result), factorial_result)
    for i in range(num):
        factorial_num = factorial_num * (i + 1)
        total = total * (i + 1)
        if total == total:
            print(i, ":", total, factorial_num)
        if my_result != factorial_result:
            errors += 1
    print("Errors:", "(" + str(num) + "):", errors)
