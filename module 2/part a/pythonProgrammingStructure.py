someVariable = 15
print(someVariable)


def someFunction():
  #this variable is LOCAL only
  someOtherVariable = "foobar"
  print(someOtherVariable)
  
def someOtherFunction(arg1, arg2):
  #this variable is LOCAL only
  result=arg1*arg2
  return result
  
someOtherVariable = someOtherFunction(4,4)
print(someOtherVariable)


def compareAndLoop():
  a, b = 10, 100
  
  # conditional flow uses if, elif, else (no case statements in python) 
  if(a < b):
    result= "a is less than b"
  elif (a == b):
    result= "a is same as b"
  else:
    result= "a is greater than b"
  print(result)
  
  x=1
  while (x < 5):
     x = x *5
     print(x)
     
  
   