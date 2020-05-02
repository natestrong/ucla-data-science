#**********************
# Variables in Python
#**********************

#E1
# Declare a variable (i.e. something that stores a value) and initialize it (i.e. set something to that variable)
someVariable = 0
print(someVariable)

#E2
# Change the value of that variable (i.e. change what was initialized before), go ahead and try 
# to reset/declare, that variable a few times, check the variable type, (use type function, i.e. is 
# it int, string, etc.)
# Note: Run each variable declaration separately
someVariable = "foobar"
someVariable = "foo"
someVariable = 111

#(remember run print for each statement separately)
print(someVariable)
print(type(someVariable))

#E3
# Global vs. local variables in functions
def someFunction():
  #this variable is LOCAL only
  someOtherVariable = "def"
  print(someOtherVariable)

someFunction()
# you should get 'NameError: name 'someOtherVariable' is not defined' (variable ONLY exists in the function)
print(someVariable) 

# This is the variable we declared earlier (it's GLOBAL)
print(someVariable)


#E4 
# Pass function to a function
def someOtherFunc(arg):
    arg=arg+1
    return arg

def someFunc(someOtherFunc):
    arg = someOtherFunc(5)
    print(arg)

#E5
#Now delete all the variables we made
del someVariable

#**********************
# Conditions in Python
#**********************

#E6
# Write a conditional in Python
def compare():
  a, b = 10, 100
  
  # conditional flow uses if, elif, else (no case statements in python) 
  if(a < b):
    result= "a is less than b"
  elif (a == b):
    result= "a is same as b"
  else:
    result= "a is greater than b"
  print(result)

#**********************
# Functions in Python
#**********************

#E7
# Define a function (i.e. takes inputs, outputs, in this case a function with NO arguments,
# NO return values)
def someFunction():
  print(1+1)

#E8
# Define a function (i.e. takes inputs, outputs, in this case a function with arguments)
# NO return values)
def someFunction(a,b):
  print(a+b)

#E9
# Define a function (i.e. takes inputs, outputs, in this case a function with arguments)
# return values)
def someFunction(a,b):
  print(a+b)
  return (a+b)

#E10
### Advanced
# Define a function (i.e. takes inputs, outputs, in this case a function with arguments)
# return values, has DEFAULT values and VARIABLE number of arguments)
def someFunction(a=1,b=1,*args):
  total = 0;
  #Multiple arg's
  for i in args:
    total = a + b + i + total
  return total

someFunction(1,1,4,5,3,3)

#**********************
# Loops in Python
#**********************

#E11
# Create a while loop
def someFunction():
  x = 0
  
  # create a while loop
  while (x < 5):
     print(x)
     x = x + 1

  # create a for loop
  for x in range(5,10):
    print(x)
  
#E12
# Create a for loop
def someFunction():
  x = 0

  # create a for loop
  for x in range(5,10):
    print(x)

#E13
### Advanced
# loop over a collection, use the enumerate() function to get index, and break and continue (generally)
# don't want to 'break' out of loops

def someFunction():

  # use a for loop over a collection
  countries = ["Brazil","Turkey","Iran","Canada","Nigeria","England","Vietnam"]
  for c in countries:

  	print ("Before breaking " + c)
  	if c == "Canada": 
  		break
  	if c != "Japan": 
  		continue
  	print(c)

  for i, c in enumerate(countries):
    print(i, c)
  

### Advanced
#**********************
# Classes in Python
#**********************

#E14
# Declare 2 classes, and instantiate (declare one of each), and manipulate their variables
# Classes are the basis as a framework for object oriented programming

class someClass():
  def method1(self):
    print ("someClass method1")
    
  def method2(self, someString):
    print ("someClass method2: " + someString)
  
      
def someFunction():
  c = someClass()
  c.method1()
  c.method2("Foobar")
  
if __name__ == "__main__":
  someFunction()
