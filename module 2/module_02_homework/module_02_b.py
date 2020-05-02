#!/usr/bin/env python
"""
Class:       UCLA Intro to Data Science
Module:      02
Assignment:  Write a Python and R Program - part b
Author:      Nathan Strong
Date:        April 19, 2020
"""

NUMBER_TO_CHECK = 100
EQUALS_NUMBER_TO_CHECK_TEXT = f'Equals {str(NUMBER_TO_CHECK)}'
LT_100_TEXT = 'fail'
GT_100_TEXT = 'pass'
IS_STRING_TEXT = 'valid'


def great_number_checker(num: int or float, text: str) -> tuple:
    if type(num) is not int and type(num) is not float:
        print(f'First argument is required to be a number, received {type(num)}.')
        return None, None

    if num < NUMBER_TO_CHECK:
        val_1 = LT_100_TEXT
    elif num > NUMBER_TO_CHECK:
        val_1 = GT_100_TEXT
    else:
        val_1 = EQUALS_NUMBER_TO_CHECK_TEXT

    val_2 = IS_STRING_TEXT if type(text) is str else None

    return val_1, val_2


if __name__ == '__main__':
    values_to_check = (
        ((5, 'some text'), (LT_100_TEXT, IS_STRING_TEXT)),
        ((100, None), (EQUALS_NUMBER_TO_CHECK_TEXT, None)),
        ((100.5, ''), (GT_100_TEXT, IS_STRING_TEXT)),
        (("some text", "5"), (None, None)),
        ((100, ", ".join(map(str, [0, 1]))), (EQUALS_NUMBER_TO_CHECK_TEXT, IS_STRING_TEXT)),
    )

    for test in values_to_check:
        print(f"Testing that {test[0]} equals {test[1]}")
        assert great_number_checker(*test[0]) == test[1]

    [print(", ".join(map(str, great_number_checker(*test[0])))) for test in values_to_check]
