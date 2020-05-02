
# coding: utf-8

# In[2]:


#example 1.1 : Print a simple text ("hello World") and comments in python

print("Hello World!")

# print("Your name")
# Note "#" is used for commenting in python
# Try printing Your name by uncommenting the print statement above


# In[3]:


#Example 2: Variables 


#Variables are simply reserved memory locations to store values
#The equal sign (=) is used to assign values on the right to variable names on the left
#Types (int, string, etc. - do NOT need to be declared in Python)

#Example 2.1 : Variable Assignment 
counter = 100                # An integer assignment
accountTotal  = 1000.1       # A floating point 
subject    = "Data Science"  # A string
boolean = True               # Boolean
empty = ""                   # Empty string (just a String), 
nullValue = None             # Null

print(counter)
print(accountTotal)
print(subject)
print(boolean)
print(empty)
print(nullValue)

##... print out the rest of the items

### Advanced
#We do not require explicit declarations within python
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(154313)


# In[1]:


#Example 2.2: Assign a value of 100 to a variable 'ap' then prit the vaue of 'ap'
ap = 100
print(ap)
#change the value of ap to 30 then print the value of 'ap'
ap = 300
print(ap)


# In[2]:


#Example 2.3: Assign a value of 100 to a variable 'ap' then print the vaue of 'ap'
ap = 100
print(ap)
#change the value of 'ap' to a string value of cat then print the value of 'ap'
#because python doesn't require strict typing you can assign different types to the same variable
#(if strictly typed this will give you an error)
ap = "cat"
print(ap)
# More on data types later


# In[16]:


#Example 2.4 : Multiple Assignment, or Assigning multiple variables at the same time 
# Assign a single value to several variables simultaneously

#Assign the value of 5 to variables a,b,c simultaneously, potentially do different things based on the variable
a = b = c = 5

#Print the value of all variables
print(a)
print(b)
print(c)


# In[4]:


#Example 3: Data Types
# Common python data types
# Numbers, Strings, List, Tuple , Dictonary 


#Example 3.1: String Type 
strExmp = 'Hello World!'
all = "string concatenation example"

# Print complete string (strExmp)
print(strExmp) 
# Print first character of the string
print(strExmp[0])  
 # Print characters starting from 3rd to 5th
print(strExmp[2:5]) 
# Print string three times
print(strExmp * 3)   
# Print concatenated string
print(strExmp + "How are you") 
# print the concatenated two string variables (strExmp and all)
print(strExmp + all)


# In[30]:


#Example 3.2: List Type 

exmList1 = [ 'Apple', 4 , 4.0, 'Orange', 77, 82 ]
exmpList2 = [100, 'Mango',100]

# Print complete list exmList1
print(exmList1)   
# Print first element of the list
print(exmList1[0]) 
#Print elements starting from 2nd till 3rd 
print(exmList1[1:3])    
# Print elements starting from 3rd element
print(exmList1[2:])   
# Prints list two times (exmpList2)
print(exmpList2 * 2) 
# Print concatenated lists (exmList1 and exmpList2)
print(exmList1 + exmpList2)

#update exmList1 1st value to 'Cat' and print it
exmList1[0] = 'Cat'
print(exmList1)

#Add a new value - 'Cool' to exmpList2 and print it
exmpList2.append('Cool')
print(exmpList2)

#remove the value 1 from exmpList2
exmpList2.remove(100)
print(exmpList2)
#Note the first occurance of the value is removed and not all 


#Try playing around with other list functions : sort, reverse, index , counts


# In[31]:


#Example 3.3 : Tuple Type 
#Tuples can be thought of as read-only lists (they cannot be changed)

tupleExmp = ( 'Kiwi', 4 , 4.0, 'Bannana', 77, 82 )
tupleExmp2 = (100, 'Carrot',100)

# Print complete list (tupleExmp)
print(tupleExmp) 
# Print first element of the list
print(tupleExmp[0])  
 # Print elements starting from 2nd till 3rd 
print(tupleExmp[1:3])     
 # Print elements starting from 3rd element
print(tupleExmp[2:]) 
# Print list two times (tupleExmp2)
print(tupleExmp2 * 2)  
# Print concatenated lists (tupleExmp2, tupleExmp)
print(tupleExmp + tupleExmp2) 

# Trying updating a tuple and see if you get an error


# In[5]:


# Example 3.4 : Dictonary Type 
dictExp = {}
dictExp['one'] = "This is one"
dictExp[2]     = "This is two"

dictExp2 = {'name': 'john','code':6734, 'dept': 'sales'}

#Print the value for the key 'one' in dictExp
print(dictExp['one'])  
#Print the value for the key 2 in dict
print(dictExp[2])    
# Print complete dictionary - dictExp2
print(dictExp2)
# Print all the keys for dictExp2
print(dictExp2.keys())  
# Print all the values for dictExp2
print(dictExp2.values())


# In[47]:


#Example 4 : Arithmetic Operations, some basic math
a = 10
b = 20

#Example 4.1 : Addition
print("a+b :",a+b)

#Example 4.2: Subtraction
print("a-b :",a-b)

#Example 4.3: Multiplication
print("a*b :",a*b)

#Example 4.4 : Division
print("a/b :",a/b)

#Example 4.5 : Modulus
print("a%b :", a%b)

#Example 4.6 : Exponent
print("2 to the power 4 :" ,2**4)


# In[45]:


#Example 5 : Comparision Operators, some basic comparisons
a = 10
b = 20
c = 10

#Example 5.1 : ==
print("a==b : ", a==b)
print("a==c :",a==c) 

#Example 5.2: !=
print("a!=b :",a!=b)
print("a!=c :", a!=c)

#Example 5.3 : Greater than, less than, greather than equal to
print("a>c :", (a>c))
print("a>=c :", a>=c)
print("a<b :", a<b)

