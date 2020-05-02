#!/usr/bin/env python
"""
Class:       UCLA Intro to Data Science
Module:      02
Assignment:  Write a Python and R Program - part c
Author:      Nathan Strong
Date:        April 25, 2020
"""
from collections import defaultdict
from typing import List, Tuple

if __name__ == '__main__':
    """
    Part A.
    """
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

    """
    Part B.
    Separate list into list of types
    """
    # List of integers and strings
    someList = [3, 'S', 'B', 21, 50.1]

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

    # Alternative - better way
    # Loop through the list and for each type, add it to a dictionary
    dictionaryOfTypes = defaultdict(list)
    for item in someList:
        dictionaryOfTypes[type(item).__name__].append(item)
    print('Dictionary of types with the values for each type as a list:')
    [print(_type, _list) for _type, _list in dictionaryOfTypes.items()]

    """
    Part C.
    Compare and contrast Python Data Structures
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
    myTuple: Tuple[str, str, int] = ('1', 'hello', 5)

    # Convenient way to return multiple values from a function
    def find_odd(numbers: List[int]) -> (List, int):
        odd_numbers = [_number for _number in numbers if (_number % 2) != 0]
        return odd_numbers, len(odd_numbers)
    oddNumbers, oddNumberCount = find_odd([1, 2, 3, 4, 5, 6, 7])
    print(f'There are {oddNumberCount} odd numbers: {oddNumbers}')
