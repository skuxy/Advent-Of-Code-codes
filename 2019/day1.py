# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
First day of AoC 2019
"""


def get_fuel(mass):
    """
    Part one
    Calculates fuel based on given mass
    """
    step1 = mass / 3
    step2 = int(step1)
    step3 = step2 - 2
    return step3


def get_additional_fuel(mass):
    """
    Part two
    Calculates fuel for originally given fuel
    """
    original_fuel = get_fuel(mass)
    if original_fuel <= 0:
        return 0

    return original_fuel + get_additional_fuel(original_fuel)


if __name__ == "__main__":
    # Part one
    assert get_fuel(12) == 2
    assert get_fuel(14) == 2
    assert get_fuel(1969) == 654
    assert get_fuel(100756) == 33583

    with open("2019/input1.txt") as input_file:
        print(sum(map(lambda x: get_fuel(int(x)), input_file)))

    # Part two
    assert get_additional_fuel(14) == 2
    assert get_additional_fuel(1969) == 966
    assert get_additional_fuel(100756) == 50346

    with open("2019/input1.txt") as input_file:
        print(
            sum(map(lambda x: get_additional_fuel(int(x)), input_file))
        )
