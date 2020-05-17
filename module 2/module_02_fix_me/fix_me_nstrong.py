#!/usr/bin/env python3
"""
Class:       UCLA Intro to Data Science
Module:      02
Assignment:  Fix Me
Author:      Nathan Strong
Date:        May 16, 2020
"""
from typing import List


def countCharactersInAString(words) -> int:
    count: int = 0
    for _ in words:
        count += 1
    return count


def reverseCharactersInAString(words: str) -> str:
    newWords: str = ''
    for character in words:
        newWords = character + newWords
    return newWords


def removeItemNFromList(listOfNumbers: List[int or float], n: int) -> List[int or float]:
    newListOfNumbers: List[int or float] = []
    i = 0
    for number in listOfNumbers:
        i += 1
        if i != n:
            newListOfNumbers.append(number)
    return newListOfNumbers


def removeItemNFromListAlt(listOfNumbers: List[int or float], n: int) -> List[int or float]:
    del listOfNumbers[n - 1]
    return listOfNumbers


def randomNumberGenerator() -> str:
    import random
    string = "is it really random?"
    randomNumber = round((random.random() * 100))
    return f"{string} {str(randomNumber)}"


if __name__ == '__main__':
    assert countCharactersInAString('nathan') == 6
    assert reverseCharactersInAString("hats are cool") == 'looc era stah'
    assert removeItemNFromList([71, 23, 81, 54, 15], 1) == [23, 81, 54, 15]
    assert removeItemNFromListAlt([71, 23, 81, 54, 15], 1) == [23, 81, 54, 15]
    assert randomNumberGenerator().startswith("is it really random?")
    assert randomNumberGenerator()[-1].isdigit()
