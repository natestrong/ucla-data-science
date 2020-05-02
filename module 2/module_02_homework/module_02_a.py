#!/usr/bin/env python
"""
Class:       UCLA Intro to Data Science
Module:      02
Assignment:  Write a Python and R Program - part a
Author:      Nathan Strong
Date:        April 12, 2020
"""
import string
import random


class PythonTutorial:
    def __init__(self):
        self.foo: string = None
        self.bar: string = None

    def define_variables(self):
        self.foo = 'foo'
        self.bar = 'bar'

    def run_a_function(self):
        lottery_numbers = range(60)
        winning_numbers = random.sample(lottery_numbers, 6)
        print(f'The Winning Lottery Numbers are: {", ".join(map(str, winning_numbers))}!')

    def if_else_statements(self):
        random_number_to_10 = random.randint(1, 10)
        print('Guess my random number 1-10')
        while True:
            guess = int(input("Enter a guess: "))
            if guess is random_number_to_10:
                print('You Win!  The answer was ' + str(random_number_to_10))
                break
            elif guess is random_number_to_10 - 1 or guess is random_number_to_10 + 1:
                print('Close, try again!')
            else:
                print('Sorry, guess again!')


if __name__ == '__main__':
    pythonTutorial = PythonTutorial()
    pythonTutorial.define_variables()
    pythonTutorial.run_a_function()
    pythonTutorial.if_else_statements()
