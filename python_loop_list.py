#Python - Loop Lists

#Loop Through a List

thelist = ["apple", "banana", "cherry"]
for x in thelist:
  print(x)

thelist = ["apple", "banana", "cherry"]
for x in thelist:
  print(x)
  if x == "banana":
    break

#Loop Through the Index Numbers
print("Loop Through the Index Numbers")
mylist = ["apple", "banana", "cherry"]
for i in range(len(mylist)):
  print(mylist[i])   
#Using a While Loop

print("Using a While Loop")
thelist = ["apple", "banana", "cherry"]
i = 0
while i < len(thelist):
  print(thelist[i])
  i = i + 1

#Looping Using List Comprehension
print("Looping Using List Comprehension")
thelist = ["apple", "banana", "cherry"]
[print(x) for x in thelist] 

#List Comprehension
print("Without list comprehension you will have to write a for statement with a conditional test inside:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)


#With list comprehension you can do all that with only one line of code:
print("With list comprehension you can do all that with only one line of code:")
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)


#newlist = [expression for item in iterable if condition == True]
print("The condition is like a filter that only accepts the items that valuate to True.")
newlist = [x for x in fruits if x != "apple"]
print(newlist)

#With no if statement:
#The condition if x != "apple"  will return True for all elements other than "apple", making the new list contain all fruits except "apple".

#With no if statement:

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

#The iterable can be any iterable object, like a list, tuple, set etc.

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits]
print(newlist)

#Using Range

newlist = [x for x in range(10)]
print(newlist)

#Accept only numbers lower than 5:

newlist = [x for x in range(10) if x < 5]
print(newlist)

#The expression is the current item in the iteration, but it is also the outcome, which you can manipulate before it ends up like a list item in the new list:

newlist = [x.upper() for x in fruits]
print(newlist)

#Set all values in the new list to 'hello':

newlist = ['hello' for x in fruits]
print(newlist)

#Return "orange" instead of "banana":
print("Return 'orange' instead of 'banana':")
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#************************Sort List Alphanumerically***************************#
print("**************Sort List Alphanumerically******************************")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

#Sort the list numerically:
print("Sort the list numerically:")
thelist = [100, 50, 65, 82, 23]
thelist.sort()
print(thelist)

#Sort Descending
print("Sort Descending")
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)   
print(thislist)

#Customize Sort Function
print("Customize Sort Function")
def myfunc(n):
  return abs(n - 50)
thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#Case Insensitive Sort
print("Case Insensitive Sort")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#Perform a case-insensitive sort of the list:
print("Perform a case-insensitive sort of the list:")
thelist = ["banana", "Orange", "Kiwi", "cherry"]
thelist.sort(key = str.lower)
print(thelist)

#Reverse Order
print("Reverse Order")
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)

#Python - Copy Lists

print("*******************************Python - Copy Lists********************************")

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print(mylist)

#Use the list() method
print("Use the list() method")
thelist = ["apple", "banana", "cherry"]
mylist = list(thelist)
print(mylist)

#Use the slice Operator
print("Use the slice Operator")
thelist = ["apple", "banana", "cherry"]
mylist = thelist[:]
print(mylist)

#Join Lists
print("Join lists")
list1 = ["a", "b" , "c"]  
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)

#Append two list

print("Append two list")
for x in list2:
  list1.append(x)

print(list1)

#Use Extend in lists

for x in list1:
  list2.extend([x])
print(list2)  


#*********************Some usefull  list methods**********************

print("*********************Some usefull  list methods**********************")

list_new = ["a", "b", "c", "d", "e"]
fruits = ['apple', 'banana', 'cherry']

print(fruits.reverse()) #Reverses the order of the list
print(fruits.sort()) #Sorts the list
print(list_new.count("a")) #Returns the number of times the specified value occurs in a list
print(list_new.index("b")) #Returns the index of the first element with the specified value
print(list_new.pop()) #Removes the element at the specified position
