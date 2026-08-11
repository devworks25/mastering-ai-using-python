#Creating Var

x = 5
y = "Hello, World!"
print(x)
print(y)

x = 4
y = "Python is awesome"
print(x)

#Casting

x = str(3)    # x will be '3'
y = int(3)  # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)

#Get the type

x = 5
y = "Hello, World!"
print(type(x))
print(type(y))

#Single or Double Quotes?
x = "John"
x = 'John'
print(x)


#PYTHON VARIABLES NAMES

myvar = "John"
my_var = "John"
_my_var = "John"
myVar = "John"
MYVAR = "John"
myvar2 = "John"


print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
myVariableName = "John"
MyVariableName = "John"
my_variable_name = "John"

#Assign Multiple Values
x,y,z = "Orange", "Banana", "Cherry"
print(x)
print(y)
print(z)

#One Value to Multiple Variables
x = y = z = "Orange"
print(x)
print(y)
print(z)

#unpack a Collection
fruits = ["apple", "banana", "cherry"]
x, y, z = fruits
print(x)
print(y)
print(z)

#Python Output Variables
x = "Python is awesome"
print("Python is " + x)

x,y,z = "Python", "is", "awesome"
print(x, y, z)  

x = "Python"
y = "is"
z = "awesome"
print(x + " " + y + " " + z)  

#Global Variables   

x = "global"

def myfunc():
  print("Python is " + x)

myfunc()

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x)

myfunc()

print("Python is " + x)

x = "awesome"
def myfunc():
  global x
  x = "fantastic"

myfunc()
print("Python is " + x)

#Python Data Types

x = "Hello World"  # str
print(type(x))
x = 20  # int
print(type(x))
x = 20.5  # float
print(type(x))
x = 1j  # complex
print(type(x))
x = ["apple", "banana", "cherry"]  # list
print(type(x))
x = ("apple", "banana", "cherry")  # tuple
print(type(x))
x = range(6)  # range
print(type(x))
x = {"name" : "John", "age" : 36}  # dict
print(type(x))
x = {"apple", "banana", "cherry"}  # set
print(type(x))
x = frozenset({"apple", "banana", "cherry"})  # frozens
print(type(x))


#Python Numbers
x = 5
y = 2.5
z = 1j
print(type(x))
print(type(y))
print(type(z))
x = 1
y = 35656222554887711
z = -3255522
print(type(x)) #int
print(type(y)) #int
print(type(z)) #int

x = 1.10
y = 1.0
z = -35.59

print(type(x)) #float
print(type(y)) #float
print(type(z)) #float

x = 35e3
y = 12E4
z = -87.7e100

print(type(x))#float
print(type(y))#float
print(type(z))#float

x = 3+5j
y = 5j
z = -5j

print(type(x))#complex
print(type(y))#complex
print(type(z))#complex

#Type Conversion

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)

#convert from float to int:
b = int(y)

#convert from int to complex:
c = int(x)

print(a)
print(b)
print(c)



print(type(a))
print(type(b))
print(type(c))


#Random Number
import random
print(random.randrange(1, 10))