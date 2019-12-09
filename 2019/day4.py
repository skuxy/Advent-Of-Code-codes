#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Day 4
Calculate password following some criteria:
* 6 digit number
* the range is given in the puzzle (168630 - 718098)
* Two adjacents digits are the same
* going from left to right, the digits never decrease,
    they only remain the same or increase

How many passwords for given range meet the criteria"""

LOWER_BOUND = 168630
UPPER_BOUND = 718098
N_OF_DIGITS = 6


# def first_criteria(number_str):
#     """ Irrelevant, as all nubers in given range meet the criteria"""
#     return True
#
#
# def second_criteria(number_str):
#     """Again, irrelevant for our quest"""
#     return True
def third_criteria(number_str):
    for i in range(1, N_OF_DIGITS):
        if number_str[i] == number_str[i - 1]:
            return True
    return False


def fourth_criteria(number_str):
    for i in range(1, N_OF_DIGITS):
        if int(number_str[i]) < int(number_str[i - 1]):
            return False

    return True


def fifth_criteria(number_str):
    """An Elf just remembered one more important detail:
    the two adjacent matching digits are not part of a
    larger group of matching digits."""
    uniq = set(number_str)

    if [x for x in map(lambda x: number_str.count(x), uniq) if x == 2]:
        return True

    return False


if __name__ == "__main__":
    # Part one
    do_satisfy_first = 0
    do_satisfy_second = 0
    for number in range(LOWER_BOUND, UPPER_BOUND):
        if third_criteria(str(number)) and fourth_criteria(str(number)):
            do_satisfy_first += 1

            if fifth_criteria(str(number)):
                do_satisfy_second += 1

    print(do_satisfy_first)
    print(do_satisfy_second)
