
# coding: utf-8

# In[2]:


# Example 1.1: functions
# Define a function isItPrime to test wether a number is prime or not.
# if the num is prime print the num
# print all the prime numbers from 2-19 using this function
# https://en.wikipedia.org/wiki/Prime_number

def isItPrime(num):
    prime = True
    for i in range(2,num):
        if(num%i == 0):
            prime = False
    if(prime):
        print(num)

for i in range(2,19):
    isItPrime(i)


# In[20]:


#Example 1.2: Function (Pass by Reference)
#Create a function which appends the values 1, 2 and 3 to the list passed. 
#Print the list inside the function and right after function call 

def updateList(listParm):
    listParm.append(1)
    listParm.append(2)
    listParm.append(3)
    print("Inside the function",listParm)

myList= ['apple','orange']
updateList(myList)
print("After function call",myList)


# In[22]:


#Example 1.3 : Keyword arguments
def printNumbers(a,b):
    print('a:',a)
    print('b:',b)

x=1
y=2
printNumbers(x,y)
printNumbers(b =x , a=y) #Note order has been changed


# In[25]:


#Example 1.4 : Default arguments
def printNumbers(a=1,b=2):
    print('a:',a)
    print('b:',b)

print('Call 1')
printNumbers()
print('Call 2')
printNumbers(a=3)
print('Call 3')
printNumbers(b=6)
print('Call 4')
printNumbers(a=7,b=8)


# In[26]:


#Example 1.5 : Return Statement
#create a function which returns the sum of two numbers passed

def calculateSum(a,b):
    return(a+b)

answer = calculateSum(4,5)
print(answer)

print(calculateSum(6,7))


# In[27]:


#Example 1.6 : Local variable vs global variable

total = 0;  #global variable
def calculateSum( a, b ):
   total = a + b #local variable
   print("Inside the function local total : ", total)
   return total


calculateSum( 10, 20 )
print("Outside the function global total : ", total)


# In[39]:


#Example 2: Modules : import
# A module can simply be a file with python code, which we can use in our source file 
# For this we use the keyword 'import'
# This helps in better organising our code 
# we can import inbuilt packages or a file created by us


# In[41]:


#Example 3.1: sets
set1 = {1, 2, 3}
print(set1)

set2 = {7.9, "Hello", (1, 2, 3)}
print(set2)


# In[46]:


#Example 3.2 : sets
a = set()
print(type(a))
a.add('apple')
a.add('b')
a.add(3.0)
a.add('sd')

print(a)
a.update([4,5], {1,6,8})

print(a)


# In[49]:


#Example 3.3 : Sets : Union 
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

#union 
print(A | B)
print(A.union(B))


# In[50]:


#Example 3.4 : Sets : Intersection 
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A&B)
print(A.intersection(B))


# In[51]:


#Example 3.5 : Sets : Difference 
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}

print(A-B)
print(B-A)
print(A.difference(B))


# In[57]:


#Example 4.1: *args and *kwargs 
# they allow us to pass variable number of arguments to a function

def printNames(a,*args):
    for arg in args:
        print("normal argument", a)
        print("values through *args :", arg)

printNames('Alison','John','Katie','Hummer')
printNames('jolly')


# In[69]:


#Example 4.2: *args and *kwargs 
def printValues(a, **kwargs):
    print ("formal arg:", a)
    for key in kwargs:
        print ("kwargs: key: %s  value: %s" % (key, kwargs[key]))

printValues(1, Apple="two", Mango=3)


# In[77]:


#Example 5: Reading from files
file = open("sample1.txt","w")
file.write("Hello! Your code is working! \n This is an example")
file.close()
file = open("sample1.txt","r")
str =file.read()
print(str)

# verify if a file was created in the directory


# In[78]:


#Example 6: Exception Handling
try:
   file = open("sample2.txt", "w")
   file.write("sample2!!")
except IOError:
   print("Error occured while writing to file.")
else:
   print("task completed successfully")
   file.close()

