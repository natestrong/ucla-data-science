#**********************
# Variables in R
#**********************

#E1
# Declare a variable (i.e. something that stores a value) and initialize it (i.e. set something to that variable)
x <- 1:10  # Put the numbers 1-10 in the variable x

#print the variables
x

#E2
# Change the value of that variable (i.e. change what was initialized before), go ahead and try 
# to reset/declare, that variable a few times, check the variable type, (use type function, i.e. is 
# it int, string, etc.)
# Note: Run each variable declaration separately
x <- "foobar"
x <- "foo"
x <- 111
y <- c(5, 7, -1, 6, 7)

#(remember run each variable separately to see output)
x
y

# List/print objects
ls()  

#E3
# Global vs. local variables in functions
f <- function(a) {
   a=1
}

f(a)

# you should get Error: object 'a' not found is not defined' (variable ONLY exists in the function)
a

# This is the variable we declared earlier (it's GLOBAL)
x

#E4
#Now delete all the variables we made
rm(x)

#**********************
# Conditions in R
#**********************

#E5
# Write a switch statement in R
compare <- function(switchTo) {

switch (switchTo,
        "PicMe" = "blah",
        "NoPicMe" = "foobar",
        "OkFine" = "foo",
)
}

# Write an if/else statement in R
compare <- function() {
a = 10
b = 100 

  if(a < b){
    result= "a is less than b"
  }
  else if (a == b){
    result= "a is same as b"
  }
  else{
    result= "a is greater than b"
  }
  print(result)
}

compare()

#**********************
# Functions in R
#**********************

#E6
# Define a function (i.e. takes inputs, outputs, in this case a function with NO arguments,
# NO return values)
f <- function() {
}

f()

#E7
# Define a function (i.e. takes inputs, outputs, in this case a function with arguments)
# NO return values)
f <- function(a, b) {
   a+b
}

f(1,2)

#E8
# Define a function (i.e. takes inputs, outputs, in this case a function with arguments)
# return values)
f <- function(a, b, c) {
   result=a+b
   return(c(result,c))
}

f(1,2,3)

#E9
### Advanced
# Define a function (i.e. takes inputs, outputs, in this case a function with arguments)
# return values, has DEFAULT values and VARIABLE number of arguments)
f <- function(a, b = 1, c = 2, d = NULL, ...) {
   result=a+b

   return(c(result,c))
}

f(1,2,3,4, 2, 4, 2)

#**********************
# Loops in R
#**********************

#E10
# Create a while loop
f <- function() {
  
  # create a while loop
  i <- 1
  while (i < 4) {
   print(i)
   i = i+1
  }

  # create a for loop
  for (number in c(1,2,3,4)) { 
    print(paste("The number is", number)) 
  }
}

### Advanced
#**********************
# Classes in R
#**********************

#E11
# Declare 1 class, and instantiate (declare one of each), and manipulate their variables
# Classes are the basis within object oriented programming
# R has an S3, S4 class

#S3 class
someClass <- function(var=TRUE)
{

        me <- list(
                someMethod = var
       )

        class(me) <- append(class(me),"someClass")
        return(me)
}

someDefaultPerson <- someClass()

setSomeMethod <- function(elObjeto, newValue)
        {
                UseMethod("setSomeMethod",elObjeto)
        }

getSomeMethod <- function(elObjeto)
        {
                UseMethod("getSomeMethod",elObjeto)
        }

someDefaultPerson <- setSomeMethod(someDefaultPerson,FALSE)

#S4 class
someOtherClass <- setClass(
  "someOtherClass", 
      representation(someField = "character"), 
  
      prototype(someField = NA_character_)

  )

someOtherClass <- new("someOtherClass", someField = "foobar")

