#!/usr/bin/env python
"""
Class:       UCLA Intro to Data Science
Module:      02
Assignment:  Write a Python and R Program - part c
Author:      Nathan Strong
Date:        April 25, 2020
"""

from typing import List, Tuple

if __name__ == '__main__':
    someVar = 1
    someOtherVar = "one"

    try:
        print(someVar + someOtherVar)
    except TypeError as e:
        print(e)
        print('When concatenating a string, an int type is not supported')

    # Use list comprehension to convert both variables to str
    someVar, someOtherVar = [str(x) for x in (someVar, someOtherVar)]
    print(someVar + someOtherVar)

    # List of integers and strings
    someList: int or str = [3, 'S', 'B', 21]

    # Split into separate lists
    listOfStrings: List[str] = []
    listOfIntegers: List[int] = []
    for x in someList:
        if isinstance(x, str):
            listOfStrings.append(x)
        elif isinstance(x, int):
            listOfIntegers.append(x)
    print('Strings: ' + ', '.join(listOfStrings))
    print('Integers: ' + ', '.join([str(x) for x in listOfIntegers]))

    """
    Compare and contrast Python Data Structures
    Python Type Hints Cheat Sheet: https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
    """
    #  1. List - An ordered collection.
    myList: List[int] = list()
    myList += range(10)
    #  Provides 'magic' functions commonly used with arrays such as:
    # len() - How many items are in list
    print(f'My list has {len(myList)} items.')
    # sum() - The sum of adding up contents of list
    print(f'The sum of my list is {sum(myList)}.')
    # slice() - Can aso be written as [:] - Slices a section of the array
    print('Every other list item:', ', '.join(str(x) for x in myList[0::2]))
    # sort() - Sort list by either default (ascending) order, or by a custom function
    myList.sort(reverse=True)
    print('List sorted in reverse', ', '.join(str(x) for x in myList))

    # 2. Tuple - Similar to lists, but are immutable (can't be modified)
    # Have less magic functions, but also take up less memory
    myTuple: Tuple[str, ...] = '1', 'hello', 'cool'

