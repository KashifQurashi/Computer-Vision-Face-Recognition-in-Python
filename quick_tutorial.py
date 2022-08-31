# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# String Assigment 
data = 'hello world'
print(data[0])
print(len(data))
print(data)

# NUmber Assigment

value = 123.1
print(value)
value = 10
print(value)


# Boolean Assigment

# Boolean

a = True

b = False

print (a, b)


# Multiple Assigment

a, b, c = 1, 2, 3

print(a, b, c)

# Non Assigment

# No value

a = None
print(a)



# Flow control statements


# If-then-else conditional statement
value = 205
if value == 99 :
    print ('That is fast')
elif value > 200:
    print ('That is too fast')
else:
    print ('That is safe')
    
    
# For-Loop

for i in range(10):
    print(i)
    


# While-Loop

i = 0
while i < 10:
    print(i)
    i += 1


# Python Data Structures

# Tuples
a = (1, 2, 3)
print(a)




# List => use the square bracket notation and can be index using array notation

myList = [1, 2, 3]
print("Zeroth value: %d" % myList[0])
myList.append(4)
print("List length: %d" % len(myList)) 
for value in myList:
    print(value )
    
    
# Dictionary : Dictionaries are mappings of names to values, like key-value pairs.
# Note: Note the use of the curly bracket and colon notations when defining the dictionary.

mydict = {'a': 1, 'b': 2, 'c': 3}
print("A value: %d" % mydict['a'])

mydict['a'] = 11
print("A value: %d" % mydict['a'])

print("keys: %s" % mydict.keys())
print("values: %s" % mydict.values())

for key in mydict.keys():
    print(mydict[key])
    
    
    
# Python Functions

# Function: The example below define a new function to calculate the sum of two values
# and calls the function with to arguments. (Ensure that you have an empty new line after indented code,
# called as white space)

# Sum Function

def mySum(x, y):
    return x + y

# Call the function
result = mySum(5, 3)
print(result)





