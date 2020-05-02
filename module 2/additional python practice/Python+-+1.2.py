
# coding: utf-8

# In[1]:


#Example 1.1: Decision Statements - if
#Supppose you need to print values based on a particular condition
# Store a value to a variable than test if the value of the fruit, than print if that fruit is found (i.e. pittaya in this case).
# If/else statement 

fruit = 'pittaya'
if(fruit == 'pittaya'):
    print('Pittaya found')
print('Hello')

#Attempt changing the value of the print statement and observe what path is executed
#Python provides no braces to indicate blocks of code, just indents and spacing (arguably one of the more painful parts of the language)

#To understand this better see the next example


# In[4]:


#Example 1.2  : Indentation and white space rules in Python

#https://docs.python.org/2.0/ref/indentation.html


# In[11]:


#Example 1.3: What if we wanted to print 'pittaya not found',
#if the fruit is not pittaya lets use the Else statement

if(fruit == 'pittaya'):
    print('Pittaya found')
else:
    print('Pittaya not found')


# In[5]:


#Example 1.4: Imagine we are calculating the split for a person based on commission
#As we know there can be different tax slabs
#for this we use elif 

commission = 10000
split = 0.0
if(commission < 10000):
    split = 100
elif(commission >= 10000 and commission <20000):   
    split = 200
elif(commission >= 20000 and commission < 30000):
    split = 300
else:
    split = 400
 
print(split)
#attempt changing values to experiment


# In[6]:


# Example 2 : Loops
# Loops are repetition structures. For example if we need to print 'pittaya' 3 times.
# We can use 3 print statements for this as below:

print('pittaya')
print('pittaya')
print('pittaya')

#or lets just do loops, we will use a for and while loop to do the same.


# In[7]:


#Example 2.1: For loop going up to 3 iterations
for num in range(0,3):
    print('pittaya')


# In[8]:


#Example 2.2 : Print numbers from 1 to 8 using for loop
for num in range(1,9):
    print(num)


# In[13]:


# example 2.3: We will do the same things using a while loop now and cast num to string (str ( ) creates casting)
num = 0
while(num < 3):
    num = num +1
    print('pittaya ' + str(num))


# In[11]:


# example 2.4: while loop : print the numbers 1 to 8
num = 1
while(num <= 9):
    print(num)
    num = num +1


# In[22]:


# example 2.5 : we can use else statements with if loops
num = 1
while(num <= 8):
    print(num)
    num = num +1
else:
    print('we are outside!')


# In[23]:


# example 2.6 : Use for loop while iterating over a list
names = ['Kofi', 'Mary','Andreas','Juanita']
for index in range(len(names)):
    print(names[index])


# In[25]:


# example 2.7 : use for loop to print the letters in a string
for letter in 'Pittaya':     
   print(letter)


# In[29]:


#Example 3.1: Nested Loops
count = 1
for i in range(1,9):
    for j in range(1, i+1):
        print(i, end='')
    print()


# In[36]:


#Example 3.2 : Find all prime numbers between 2 to 19 and print them 

for num in range(2,20):
    prime = True
    for i in range(2,num):
        if(num%i == 0):
            prime = False
    if(prime):
        print(num)
        
# try doing the same using a while loop

