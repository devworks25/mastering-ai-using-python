#Common if statmenet

import numbers


a = 23
b = 47

if a > b:
    print("A is winner")
else:
    print("B is winner")



#Logged in user

loggedIn = 1

if loggedIn:
    print("Yes logged in")


#If elif

a = 33
b = 33

if b < a:
    print("A is winner")
elif a == b:
    print("A is equal to B")
else:
    print("B is winner")

#Multiple elif

score = 75

if score >= 90:
  print("Grade: A")
elif score >= 80:
  print("Grade: B")
elif score >= 70:
  print("Grade: C")
elif score >= 60:
  print("Grade: D")

#The Else Keyword

a = 200
b = 33

if b < a:
    print("A is winner")
elif a == b:
    print("A is equal to B")
else:
    print("B is winner")

#Else Without Elif

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")


#another else if

numbers = 7

if numbers % 2 == 0:
  print("The number is even")
else:
  print("The number is odd")



#Shorthand if else

a = 50
b = 7

if a > b : print("How are you")

#One-line if/else that prints a value:
print(b) if b < a else print(a)

#Assign a Value With If ... Else

a = 10
b = 20

bigger = a if a > b else b

print("Bigger is ", bigger)

#Multiple Conditions on One Line
#variable = value_if_true if condition else value_if_false

a = 330
b = 440

print("A") if a > b else print("B") if a == b else print("B")

x = 15
y = 20
max_value = x if x > y else y
print("Maximum value:", max_value)

#Setting a default value:

username = ""
display_name = username if username else "Guest"
print("Welcome,", display_name)


#Logical operastor

#Test if a is greater than b, AND if c is greater than a:

a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")

#Test if a is greater than b, OR if a is greater than c:

a = 200
b = 33
c = 500
if a > b or a > c:
  print("At least one of the conditions is True")

#The not Operator

a = 33
b = 200
if not a > b:
  print("a is NOT greater than b")

#Combining Multiple Operators
age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
  print("Discount applies!")

#Using Parentheses for Clarity

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
  print("Great day for outdoor activities!")

#User authentication check:

username = "Tobias"
password = "secret123"
is_verified = True

if username and password and is_verified:
  print("Login successful")
else:
  print("Login failed")

#Range checking with logical operators:

score = 85

if score >= 0 and score <= 100:
  print("Valid score")
else:
  print("Invalid score")

#Nested If Statements

x = 41

if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

#Checking multiple conditions with nesting:

age = 25
has_license = True

if age >= 18:
  if has_license:
    print("You can drive")
  else:
    print("You need a license")
else:
  print("You are too young to drive")

#Multiple Levels of Nesting


score = 85
attendance = 90
submitted = True

if score >= 60:
  if attendance >= 80:
    if submitted:
      print("Pass with good standing")
    else:
      print("Pass but missing assignment")
  else:
    print("Pass but low attendance")
else:
  print("Fail")

#Nested If vs Logical Operators

temperature = 25
is_sunny = True

if temperature > 20:
  if is_sunny:
    print("Perfect beach weather!")

#Could also be written with and:

temperature = 25
is_sunny = True

if temperature > 20 and is_sunny:
  print("Perfect beach weather!")

#Use pass statement
#if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

age = 20

if age < 18:
  pass # TODO: Add underage logic later
else:
  print("Access granted")

score = 85

if score > 90:
  pass # This is excellent
print("Score processed")


#pass with Multiple Conditions
value = 50

if value < 0:
  print("Negative value")
elif value == 0:
  pass # Zero case - no action needed
else:
  print("Positive value")