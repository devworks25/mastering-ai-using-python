#Tuples allow duplicate values:

thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

#lenth of tuple
print(len(thistuple))

#create tuple with one item
thistuple = ("apple",)
print(type(thistuple))

#Not a tuple
thistuple = ("apple")
print(type(thistuple))

#Tuple Items - Data Types
tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#tuple with mixed data types
print("Tuple with mixed data types")
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)
print(type(tuple1))

#Tuple constructor
print("Tuple constructor")
thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)
print(thistuple.__sizeof__)

#Print all methods 
# for x in dir(tuple):
#     print(x)

#Access Tuple Items
#You can access tuple items by referring to the index number, inside square brackets:

thistuple = ("apple","banana","cherry")
print(thistuple[1])

#Negative Indexing
#-1 refers to the last item, -2 refers to the second last item etc.

thistuple = ("apple","cherry","banana")
print(thistuple[-1])

#Range of Indexes
thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")
print(thistuple[1:3])
print(thistuple[:4])
print(thistuple[4:])
print(thistuple[-4:-1])#Specify negative indexes if you want to start the search from the end of the tuple:

#Check if Item Exists
print("*******************Check if Item Exists*****************************")

print("check item exist or not")

thistuple = ("apple","banana","cherry","orange","kiwi","melon","mango")

if "apple" in thistuple:
    print("Yes Apple existed in this tuple")


#**********************Update Tuples***********************************/

print("#**********************Update Tuples***********************************#")

print("***********************Change Tuple Values******************************")

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#Add Items in tuples
thistuple = ("apple", "banana", "cherry")

y = list(thistuple)
y.append("Horse")
thistuple = tuple(y)

print(thistuple)

#Add tuple to a tuple

thistuple = ("apple", "banana", "cherry")
thistuple_y = ("Ekta",)
thistuple += thistuple_y
print(thistuple) 

#Remove item from tuple
print("Remove item from Tupple")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)

print("#del this tupple")

tempTuple = ("apple", "banana", "cherry")
#del tempTuple # When you do uncomment it will remove from tupple
print(tempTuple)


#********************************Unpack a tupplle ************************************#
print("================Unpack Tupple=============")

fruits = ("apple","banana","cherry")

(green,yellow,red) = fruits
print(green)
print(yellow)
print(red)

#Using Asterisk*

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green,yellow,red, *remain) = fruits

print(green,yellow,red,remain)


#Add a list of values the "tropic" variable:

(green , *tropic , red ) = fruits

print(green)
print(tropic)
print(red)


#****************************Loop Tuples***************************

thistuple = ("apple","banana","rice")

for x in thistuple:
    print(x)

#Loop Through the Index Numbers

for x in range(len(thistuple)):
    print(x)
    print(thistuple[x])

#Using a While Loop

thistuple = ("A","B","C","D")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i = i + 1

#Join Tupples : Join Two Tuples

var_a = ("a","b","c","d")
var_b = (1,2,3,4)
var_c = var_a + var_b
print(var_c)

#Multiply Tuples

var_mul = ("A","B","C")
mytuple = var_mul * 2
print(mytuple)

#Tuples Methods
thistuple = (1, 3, 7, 8, 7, 5, 4, 6, 8, 5)
x = thistuple.count(5)
x_index = thistuple.index(8)
print(x)
print(x_index)