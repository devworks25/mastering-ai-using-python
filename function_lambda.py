Lamda Function

#lambda arguments : expression

#Add 10 to argument a, and return the result:
x = lambda a:a+10
print(x(5))

#Multiple Args : Multiply argument a with argument b and return the result:

xx = lambda a,b : a * b
print(xx(5,6))


#Summarize argument a, b, and c and return the result:

xxx = lambda a,b,c : a+b*c
print(xxx(3,4,5))
print(xxx(3,4,5))
print(xxx(3,4,5))

def function1(n):
    return lambda  a : a * n
mydoubler = function1(2)

print(mydoubler(111))



def function2(a, b):
    check = lambda a, b: print("A is great") if a >= b else print("B is big")
    check(a, b)

function2(7,7)

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))
print(mytripler(22))

#Lambda with Built-in Functions

#Double all numbers in a list:

numbers: list[int] = [1, 2, 3, 4, 5]# Explicit
#numbers = [1, 2, 3, 4, 5]
doubled = list(map(lambda x: x * 2, numbers))
print(doubled)

#Using Lambda with filter()
numbers = [1,2,3,4,5,6,7,8]
odd_numbers = list(filter(lambda x : x % 2 != 0 , numbers))
print(odd_numbers)

#Using Lambda with sorted()

students  = [('Email',25),('Tobias',56),('Lina',50)]
sorted_student = sorted(students,key=lambda x: x[1])
print(sorted_student)

#Sort strings by length:
words = ["apple","pie","banana","cherry"]
sorted_words = sorted(words,key=lambda x: len(x))
print(sorted_words)