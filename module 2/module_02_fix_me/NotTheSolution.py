#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: ael-annan
"""

#### REPLACE all ??? with the solution/fix

### 1 ###
# This is broken...please fix me! #

# declare function name, accept one argument
def countCharactersInAString(words):
  # we'll have to initialize the variable to 0 (we'll need something to 'store' the count later)
  count = 0  
  #let's perform the loop here, extracting a character from each part of the words argument
  for ??? in words:
    #use flow/control logic
    if len(chars) != 0:
      #increment the counter
      count = ??? + 1
  #return the result
  return ???


countCharactersInAString("hats are cool")
#13

### 2 ###
# Is it still broken, oh, it's changed... #

# declare function name, accept one argument
def reverseCharactersInAString(words):
  # we'll have to initialize the variable to store a new string, hence the empty string
  newWords=???  
  #let's perform the loop here, extracting a character from each part of the words argument
  for chars in words:
    #use flow/control logic
    if len(chars) != ???:
      #append the characters now naturally reversed to the original variable
      newWords = chars+newWords
  #return the result
  return ???


reverseCharactersInAString("hats are cool")
#'looc era stah'

### 3 ###
# And let's fix this...

# declare function name, accept two arguments
def removeItemNFromList(listOfNums, n):
  # initalize variables to an empty list, and counter to 0 (we'll use the counter)
  newListOfNums = []
  i=???
  #let's perform the loop here, iterate through the list
  for number in listOfNums:
    #the counter used to 'count' up till n, n is where we want to EXCLUDE the number
    i=i+???;
    #use flow/control logic, in this case ONLY if we haven't hit n let's create the new list
    if (len(listOfNums) != 0) and (i !=n) :
      #append the characters with n variable removed
      newListOfNums.append(number)
  #return the result
  return ???


removeItemNFromList([71, 23, 81, 54, 15], 1)
#[23, 81, 54, 15]


### 4 ###
# Just one more

#pull in, import, call into the name space the given library/package
import random
# declare function name, no arguments
def randomNumberGenerator():
  #initalize variable to the string
  string="is it really random?"
  #random variable being produced from a library
  ??? = random.random()
  #empty string
  space=""
  #concatenate all the string
  result=string+???+str(random.random())
  #return the result
  return ???


randomNumberGenerator()
#'is it really random? 0.28853753497094137'
#(and well, its' psuedo random so the number above will change)