# true or false
# https://www.w3schools.com/python/python_booleans.asp
print("true: ", 10 > 9)
print("false: ", 10 == 9)
print("false: ", 10 <= 9)
a = 200
b = 33
if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")

# the bool() function allows you to evaluate any value
# give true or false in return. 
print(bool("hello"))
print(bool(15))

# bool()-> most values are true except empty string and 0
# any list tuple, set and dictionalyr are true
# except empty ones.
# false, non, 0(int), 0.0(float), ""(empty string)
# [] empty list, {} empty dictionary, () empty tuple, 
# and set() empty set.

"""
This is the test section of github commit (do not worry a lot)
"""

my_list = []
if bool(my_list):
    print("The list is not empty")
else:
    print("The list is empty")

class myclass():
    def __len__(self):
        return 0

myObj = myclass()
print(bool(myObj))

def myFunction():
    return True
print(myFunction())

if myFunction():
    print("YES")
else:
    print("NO!")

x = 200
print(isinstance(x, int))

# python operator
# ** expenetiation
# // floor division
# what is >>= and <<= : right and left shift bitwise
# operator. 
# logical operator, and or not
# not(x<5 and x<10)???

# identity operator
# is: x is y
# is not: x is not y

# memebership operator: 
# x in y: return true if a sequence with x
#s x not in y: return true if not in

# Bitwise operators
# bitwise operator are used to compare(binary) numbers
# & : x & y
# | :
# ^: sets each bits to 1 if only one of two bits is 1?
# x^y?????
# ~: invert all the bits
# << and >> 


