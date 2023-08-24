#datatype
"""
python Data Types
built-in data types
text
numeric
sequence
mapping
set
boolean
binary
none
what is mapping datatype?(python mapping types)
the mapping objects are used to map hash table values
to arbiary objects. 
mapping types called dictionary. 

https://docs.python.org/3/library/stdtypes.html
built-in types

mapping type - dict
a mapping object maps hashable value to arbitarary objects. 
mappings are mutable objects. 

what is mutable? liable to change
what is arbitrary? based on random choice
"""
# mapping datatype?
"""
how to use mapping datatype in python?
dict(), dictionary
* used to store values in key-value-pair
* does not allow duplicates
* changeable collection

Dictionaries are used to store data values in 
key:vlaue pairs

a dictionary is a collectioni which is ordered. 

changeable, but not duplicatable. 

thisdict = {
 "brand": "Ford",
 "model": "Mustang"
}

to determine how many items a dictionary has, 
use the len()
len(thisdict)
Dictionary itmes-> can be of any data types. 

From Python's perspective, 
dictionaries are defined 
as objects with the data type 'dict':
print(type(thisdict))
return is <class 'dict'>
exampl 1. 
my_dict = idct(a = 1, b = 2, c = 3)

example 2. 
my_list = ~~~
my_dict = dict(my_list)


example 3. 
key1 = 'a'
key2 = 'b'
value1 = 1
value2 = 2

my_dict = dict([(key1, value1),(key2, value2)])

the key difference between using dict() and creating
a dictionary with curly braces'{}' is using dict() allows
you to create a dctionary using variables or other dynamic
values. 
"""

#getting the data type. 
x = 5
# not good usage example for is
if type(x) is int:
    # is poerator compare the identity of two objects
    # return true if the two objects are the same
    # object in memory. 
    print(f"The type is {type(x)}")
else:
    print("this is not integer")
    
if isinstance(x, int):
    # check used to check if an object belongs to a
    # certain class or data type. 
    # class or type -> return 
    # first check object -> second type or class
    print("The type is integer")
else:
    print("this is not integer")
print('')
print("the datatype List")
x0 = None
x1 = "HelloWord"
x2 = 20
x3 = 20.5
x4 = 1j
x5 = ["apple", "banana", "cherry"]
x6 = ("apple", "banana", "cherry")
x7 = range(6)
x8 = {"name":"john", "age": 36}
x9 = frozenset({"apple", "banana", "cherry"})
x10 = True
x11 = b"hello" #bytes?
x12 = bytearray(5)
x13 = memoryview(bytes(5))

# for from 0 to 13, 14 not included 
for i in range(0, 14):
    print(f"x{i}: ", type(eval(f"x{i}")))

# eval() -> is a bult-in function that is used to 
# evaluate a string as a statement
# eval() function takes a string as an argument, and 
# return the result of evaluating expression or statement

# the 'f' before string is used to create an f-string. 
# what is f-string
# a formatted string literal in python 

# python Numbers

x = 1 # int
y = 2.8 # float
z = 1j # complex root -1 or j^2 = 1

# complex -> real part and imaginary part 1 + j
# z = complex (2, 3)
# z = 2 + 3j
# study for imaginary number
# https://www.w3schools.com/python/python_numbers.asp
print(type(x))
print(type(y))
print(type(z))
# example of int integer, whole number
# positive or negative, without decimal
x1 = 1
y1 = 2345634252345234534
z1 = -342345
print(type(x1))
print(type(y1))
print(type(z1))
x2 = 1.23
y2 = 10.1
z2 = -35.35
print(type(x2))
print(type(y2))
print(type(z2))
x3 = 45e4
y3 = 12E4
z3 = -878.3e100
print(type(x3))
print(type(y3))
print(type(z3))

# type conversion
# int(), float(), and complex()

x = 1
y = 2.8
z = 1j

a = float(x)
b = int(y)
# 1 + j
c = complex(x)

print(a)
print(b)
# 1 + j
print(c)
print(type(a))
print(type(b))
print(type(c))

import random
print(random.randrange(1, 10))

# python Casting
x = int(1)
y = int(2.8)
z = int("3") 
x = float(1)
y = float(2.8)
z = float("3.0")
w = float("4.2")
x = str("s1")
y = str(2)
z = str(3.0)











