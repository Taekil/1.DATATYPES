#this is tutorial review of python3 w3schools.com -> python  tutorial
#variables.py
#date: feb23th2023

x = 5
y = "john"

print(x)
print(y)

x = 4 #x is of type int
x = "sally" #x is now of type str

#casting
x = str(3) # x will be '3'
y = int(3) # y will be 3
z = float(3) # z will be 3.0

#you can get the datatype of a variable with type() function
x = 5;
y = "john"
print(type(x))
print(type(y))

#single or double quotes? is the same

#variableNames
myVar = "John"
my_var = "John"
_my_var = "John"
myvar = "John"
MYVAR = "John"
myvar2 = "John"

#camel case: myVariableName
#Pascal case: MyVariableName
#Snake case: my_variable_name

x, y, z = "Orange", "is", "new Black"
print(x)
print(y)
print(z)

x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack a collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

ap, ba, ch = fruits
print(ap)
print(ba)
print(ch)

#python output variables
x = "Python3 is awesome"
print(x)

x = "Python3"
y = "is"
z = "Awesome"

print(x, y, z)

print(x + y + z)

x = 5;
y = "John"
print(x, y)
#print(x + y) -> errored

