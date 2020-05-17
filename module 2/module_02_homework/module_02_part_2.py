#!/usr/bin/env python
"""
Class:       UCLA Intro to Data Science
Module:      02
Assignment:  Write a Python and R Program - part c
Author:      Nathan Strong
Date:        April 25, 2020
"""
import sys
from collections import defaultdict, Counter
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
    Separate list into two lists of types.
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
    Compare and contrast Python Data Structures.
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

    # 3. Dictionary - A collection of key, value pairs. (Generally) unordered.
    myDictionary = {'Nathan': 100, 'Jacob': 500, 'Billy': 1000}
    if 'Nathan' in myDictionary:
        print(f'Nathan has value {myDictionary["Nathan"]}')
    # You can also set a default return value if they key is not found using .get()
    kassandraValue = myDictionary.get('Kassandra', 0)
    print(f'Kassandra has a value of {kassandraValue}')

    # 4. Set - Represents a collection of distinct elements
    mySet = set()
    mySet.add(1)       # s is now {1}
    mySet.add(2)       # s is now {1, 2}
    mySet.add(2)       # s is still {1, 2}

    """
    Part D.
    Specialized datatypes are not automatically imported and contain more specific functionality.
    """
    # defaultdict - subclass of dict, fills in missing values with a default value
    def missing_value():
        return 'missing value'
    myDefaultdict = defaultdict(missing_value)
    myDefaultdict['Maxwell'] = 'cat'
    print(myDefaultdict['Maxwell'])
    print(myDefaultdict['Sophie'])

    # Counter - turns a sequence of values into a mapping of keys to counts
    someNumbers = 0, 2, 4, 2, 8, 5, 0, 2, 4, 0
    myCounter = Counter(someNumbers)
    mostCommon, mostCommonCount = myCounter.most_common(1)[0]
    print(f'myCounter has the value {mostCommon} the most at {mostCommonCount} times')

    # Matplotlib - A Python library which has to be imported into virtual environment
    def testMatplotlib():
        from matplotlib import pyplot as plt
        players: List[str] = ['Messi', 'Mbappe', 'Salah', 'Lewandowski', 'Mane']
        goals: List[int] = [36, 33, 22, 22, 22]

        # Create a bar chart, player on x axis, goals on y-axis
        plt.bar(players, goals)
        plt.title('Goals scored in 2019')
        plt.show()

    if 'matplotlib' in sys.modules:
        testMatplotlib()

    """
    Part E.
    Write a function that separates out the negative and positive integers in a list.
    """
    listWithPositiveAndNegative = range(-15, 15, 3)
    negativeNumbers: List[int] = []
    positiveNumbers: List[int] = []
    for value in listWithPositiveAndNegative:
        if value < 0:
            negativeNumbers.append(value)
        elif value > 0:
            positiveNumbers.append(value)

    print(f'negative: {negativeNumbers}\npositive: {positiveNumbers}')