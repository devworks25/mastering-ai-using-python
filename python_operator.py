#Arithmetic Operators

#Here is an example using different arithmetic operators:
x = 15
y = 4

print(x + y)
print(x - y)
print(x * y)
print(x / y)
print(x % y)
print(x ** y)
print(x // y)

#Floor division always returns an integer.
x = 12
y = 5

print(x // y)

#Assignment Operators
numbers = [1, 2, 3, 4, 5]

if (count := len(numbers)) > 3:
    print(f"List has {count} elements")

#The Ternary Operator
num = 6

x = "WEEKEND!" if num > 5 else "Workday"

print(x)

#Instead of Elif:

num = 6

x = "Fri" if num == 5 else "Sat" if num == 6 else "Sun" if num == 7 else "weekday"

print(x)

#Comparison Operators
x = 5
y = 3

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical Operators
x = 5
print(x > 3 and x < 10) 
print(x > 3 or x < 4)
print(not(x > 3 and x < 10))

#identity operators
x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
print(x is y)
print(x == y)

#Membership Operators
x = ["apple", "banana"]
print("banana" in x)
print("pineapple" not in x) 

#Bitwise Operators
x = 5
y = 3   
and_operator = x & y
or_operator = x | y
xor_operator = x ^ y    
print("Bitwise AND:", and_operator)
print("Bitwise OR:", or_operator)
print("Bitwise XOR:", xor_operator)   

#Operator Precedence
print((6 + 3) - (6 + 3))
print(100 + 5 * 3)

#Precedence Order   
#() # this haves the highest precedence
#** # this haves the second highest precedence
#+ - # this haves the third highest precedence
#+x  -x  ~x have the fourth highest precedence
#*  /  //   # this haves the fifth highest precedence
