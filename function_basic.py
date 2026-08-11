#function

def my_function():
    print("This is what i build")

my_function()
my_function()

#fahrenheit to celcius

def fahrenheit_to_celcius(fahrenheit):
    return (fahrenheit - 32) * 5/9

print(fahrenheit_to_celcius(77))
print(fahrenheit_to_celcius(95))
print(fahrenheit_to_celcius(50))

#Return function

def get_greeting():
    return "Hello from a function"

message = get_greeting();
print(message)
print(get_greeting())

#The Pass Statement

def my_function():
    pass

#Python Function Arguments---*******---------------

def my_function(fname): # fname is a parameter
    print(fname+ "Refsnes")

my_function('hello'); # "hello" is an argument

#Multi Argument

def age_function(dob=11, mon="march", ymd=1986): #Function With Default param
    print(f"My Bithday date is {dob}")
    print(f"My Bithday month is  {mon}")
    print(f"My Bithday Year is {ymd}")
    print(f"So My complete birthday is {dob} {mon} {ymd}")

age_function(29, "July", 1995)

age_function()

#Keyword Arguments

def argument_function(animal,name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

argument_function(animal = "dog", name = "Buddy")
argument_function(name = "Buddy", animal = "dog")
argument_function("Buddy","Willson")


#Positional Arguments

def positional_function(animal, name):
  print("I have a", animal)
  print("My", animal + "'s name is", name)

positional_function("dog", "Buddy")

#Mixing Positional and Keyword Arguments

def my_function(animal, name, age):
  print("I have a", age, "year old", animal, "named", name)

my_function("dog", name = "Buddy", age = 5)

#Passing Different Data Types

def my_function(fruits):
  for fruit in fruits:
    print(fruit)

my_fruits = ["apple", "banana", "cherry"]
my_function(my_fruits)

#Sending a dictionary as an argument:

def disct_function(person):
   print("Name:",person['name'])
   print("Age:",person['age'])

my_person = {"name": "Deepak","age":40}
disct_function(my_person)

# Positional Arguments

def positional_function(animal,name):
   print("I have a ",animal)
   print("My",animal + "'s name is ",name)

positional_function('Renu','Dog')
   
# Switching the order changes the result:

positional_function('Dog','Renu')

# Mixing Positional and Keyword Arguments

def mixing_function(animal,name,age):
   print(f"I have a {age} year old {animal} his name {name}")

mixing_function('Dog',name="Buddy",age=5);

#Passing Different Data Types

def diffrent_data_types(fruits):
   for fruit in fruits :
      print(fruit)
my_fruits = ["apple", "banana", "cherry"]
diffrent_data_types(my_fruits)

#Sending distionary as args

def dif_args_function(person):
        print("Name:", person["name"])
        print("Age:", person["age"])
my_person = {"name": "Emil", "age": 25}
dif_args_function(my_person)


#Fib function
def fib(n=2000): # Write Fibonacci   series less than n
   """ Print a Fibonaci series less then n"""
   a,b = 0,1
   while a < n:
      print(a,end='')
      a,b = b , a+b
      print()

fib();

 # return Fibonacci series up to n
def  fib2(n):
    """ Return a list of containing the Fibonacci series up to a"""
    result = []
    a,b = 0,1
    while a < n :
        result.append(a)
        a,b = b,a+b
    return result

f100 = fib2(100)
print(f100);

#Return Diffrent data types

def return_function():
   Fruits = ['apple','banana','cherry']
   return Fruits

print(return_function())


#Tuple Return Function

def tuple_function():
   return (10,20)
x,y = tuple_function()
print("X:",x)
print("Y:",y)

#Positional-Only Arguments

def my_positional_function(name, /):
   print("Hello",name)

my_positional_function('emli So')

#Keyword-Only Arguments

def keyword_only_function(*,name):

   print("Hello",name)

keyword_only_function(name="Emil")

#Combining Positional-Only and Keyword-Only

def combining_positional_function(a,b,/,*,c,d):

   return a+b+c+d

result  = combining_positional_function(5,10,c=15,d=20)
print(result);


# Function from python website

# Default Argument Values

def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        reply = input(prompt)
        if reply in {'y', 'ye', 'yes'}:
            return True
        if reply in {'n', 'no', 'nop', 'nope'}:
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)
# ask_ok('Do you really want to quit?') 
# ask_ok('OK to overwrite the file?', 2) # it will give you 3 times retry
#ask_ok('OK to overwrite the file?', 2, 'Come on, only yes or no!')


#Keyword Arguments

def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword

#Positional only function

def pos_only_args(args,/):
   print(args)

def kwd_only_arg(*,arg):
   print(arg)

def combined_example(pos_only,/,standard,*,kwd_only,another_kwd_only):
   print(pos_only,standard,kwd_only,another_kwd_only)

pos_only_args(1)
#pos_only_args(args=1)

#combined_example(1, 2, 3, 4)
combined_example(1, 2, kwd_only=3,another_kwd_only=5)
combined_example(1, standard=2, kwd_only=3,another_kwd_only=5)

def foo(name, **kwds):
    return 'name' in kwds


#foo(1, **{'name': 2})

 #Arbitrary Argument Lists,
 #When you don't know how many positional arguments will be passed:

#*args and **kwargs

#Arbitrary Arguments - *args

# def my_arg_function(*kids):
#   print("The youngest child is " + kids[0] + kids[1] + kids[2])

# my_arg_function("Emil", "Tobias", "Linus")


def my_second_function(*args):
  print("Type:", type(args))
  print("First argument:", args[0])
  print("Second argument:", args[1])
  print("All arguments:", args)

my_second_function("Emil", "Tobias", "Linus")

def my_third_function(greeting, *names):
  for name in names:
    print(greeting, name)

my_third_function("Hello", "Emil", "Tobias", "Linus")
#Arbitrary Arguments are often shortened to *args in Python documentation.

#Practical Example with *args

def my_args_practical(*numbers):
  total = 0
  for num in numbers:
    total += num
  return total

print("My Args Function")
print(my_args_practical(1,2,3))
print(my_args_practical(10, 20, 30, 40))
print(my_args_practical(5))

#Another Example Finding the maximum value
print("Finx Max Numbers")
def my_max_value_args_function(*numbers):
  if len(numbers) == 0:
    return None
  max_num = numbers[0]
  for num in numbers:
    if num > max_num:
      max_num = num
  return max_num

print(my_max_value_args_function(10.60,70))

#Arbitrary Keyword Arguments - **kwargs

def my_kwargs_function(**kid):
   print("His last name is "+kid['lname'])

my_kwargs_function(fname="Deepak",lname="Kumar")
   

def my_another_kwarg_function(**myvar):
   print("Type:",type(myvar))
   print("Name:",myvar["name"])
   print("Age:",myvar["age"])
   print("All data:", myvar)


my_another_kwarg_function(name="Tobias",age=30,city="Bergan")

#Using **kwargs with Regular Arguments

def my_kwarg_regular(username, **details):
   print("UserName:",username)
   print("Additional Details")
   for key,value in details.items():
      print(" ",key + ":",value)
   
my_kwarg_regular("email123",age="25",city="Oslo",hobby="coding")  

#Combining *args and **kwargs
# The order must be:

# regular parameters
# *args
# **kwargs

def my_args_and_kwargs_function(title, *args, **kwargs):
    print("Title:", title)

    for arg in args:
        print("Arg:", arg)

    for key, value in kwargs.items():
        print(f"{key}: {value}")

my_args_and_kwargs_function(
    "User Info",
    "Emil",
    "Tobias",
    age=25,
    city="Oslo"
)

#Unpacking Arguments

#The * and ** operators can also be used when calling functions to unpack (expand) a list or dictionary into separate arguments.
def my_unpack_function(a,b,c):
   return a+b+c

numbers = [1,2,3]
result = my_unpack_function(*numbers)# Same as : my_unpack_function(1,2,3)
print(result)

#Unpacking Dictionaries with **

def unpacking_dict_function(fname,lname):
   print("Hello",fname,lname)

person = {"fname":"Emil","lname":"Refsnes"}
unpacking_dict_function(**person)## Same as: unpacking_dict_function(fname="Emil", lname="Refsnes")