'''
CIS 122 Fall 2018 Lab 7
Author: Jacob I Rammer
Credit: N/A
Description: Lists
'''
import random


def new_list_variable(t):
    new_t = t[:]
    new_t.sort()
    return new_t


def gen_random_integer_list(num, start_range=1, end_range=100, sort_list='N'):
    """Generate random integer list
    :param num:
    :param start_range:
    :param end_range:
    :param sort_list:
    :return:
    """
    t = []
    if num <= 0:
        print("num must be > 0")
    elif not isinstance(num, int):  # if num is not a int
        print("num must be an integer")
    elif not isinstance(start_range, int) or not isinstance(end_range, int):  # if num is an int
        print("start_range and end_end range must be integers")
    else:
        for i in range(num):
            r = random.randint(start_range, end_range)
            t.append(r)  # add random number to list

            if sort_list.upper() == "Y":
                t.sort()
        return t


t = gen_random_integer_list(100)


def get_high_score(t):
    """
    Get the high score of the list
    :param t: list
    :return: high score, -1 if not a list, 0 if empty
    """
    if not isinstance(t, list):
        print("List argument expected")
        return -1
    elif not len(t) > 0:
        print("List should not be empty")
        return 0
    else:
        score = 0
        new_t = new_list_variable(t)
        score = new_t[-1]
        return score


def get_low_score(t):
    """
    get the low score of the list
    :param t: list
    :return: low score, -1 if not a list, 0 if empty
    """
    if not isinstance(t, list):
        print("List argument expected")
        return -1
    elif not len(t) > 0:
        print("List should not be empty")
        return 0
    else:
        score = 0
        new_t = new_list_variable(t)
        score = new_t[0]
        return score


def get_mean_score(t):
    """
    Get the mean of the list
    :param t: list
    :return: mean, -1 if not a list, 0 if empty
    """
    if not isinstance(t, list):
        print("List argument expected")
        return -1
    elif not len(t) > 0:
        print("List should not be empty")
        return 0
    else:
        mean = sum(t) / len(t)
        print(mean)


def get_median_score(t):
    """
    get the median of the list
    :param t: list
    :return: median
    """
    new_t = new_list_variable(t)
    median = len(t) // 2
    if len(t) % 2:
        return new_t[median]
    else:
        median = (new_t[median] + new_t[median - 1]) / 2
        return median


def count_range(t):
    """
    find the number of A's, B's, etc.
    :param t: list
    :return: -1 if not a list or list are not ints or start is greater than end, numbers of a b c d f
    """
    new_t = new_list_variable(t)
    a = b = c = d = f = 0

    # guardian code
    if not isinstance(t, list):
        print("List argument expected")
        return -1
    elif not isinstance(t[1], int) or not isinstance(t[-1], int):
        print("start and end must be integers")
        return -1
    elif new_t[1] > new_t[-1] or new_t[1] == new_t[-1]:
        print("start must be < end")
        return -1
    elif len(new_t) == 0:
        return 0
    # end guardian code

    for score in new_t:
        if 100 >= score >= 90:
            a += 1
        elif 89 >= score >= 80:
            b += 1
        elif 79 >= score >= 70:
            c += 1
        elif 69 >= score >= 60:
            d += 1
        elif score < 60:
            f += 1
    return a, b, c, d, f


def list_range(t):
    """
    print the results
    :param t: list
    :return: void
    """
    a, b, c, d, f = count_range(t)
    print("A - " + str(a), "\nB - " + str(b) + "\nC - " + str(c) + "\nD - " + str(d) + "\nF - " + str(f))


print(new_list_variable(t))
list_range(t)
print(get_low_score(t))
print(get_high_score(t))
get_mean_score(t)
print(get_median_score(t))
count_range(t)
