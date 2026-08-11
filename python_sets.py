#*****************************Python Sets******************************

from ctypes.wintypes import PINT


print("#*****************************Python Sets******************************")

simpleSet = {"apple", "banana", "cherry"}
print(simpleSet)
#Duplicates Not Allowed
#True is considered as same value 
#False and 0 is considered the same value:
myvar = {"a","b","c","D","D",True,1,2,False,0}
myvar2 = {}
print(myvar)
#Set Length
print(len(myvar))

#Set items can be of any data type:

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}


#A set with strings, integers and boolean values:
set1 = {"abc", 34, True, 40, "male"}

#Get Type of set

print(type(set1))


#Set Constructure

myset = set(("Apple","Banana","Cherry"))
print(myset)

#Python - Access Set Items

for x in myset:
    print(x)

#Print True or False if value exist 
print("Cherry" in myset)
print("Cherry" not in myset)


#Add Set Items
thisset = {"apple", "banana", "cherry"}
thisset.add("Orange")
print(thisset)


#********************Add Sets*********************
thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
mylist = ["kiwi", "orange"]
thisset.update(tropical)

print(thisset)

#Add Any Iterable

thisset.update(mylist)

print(thisset)


#*********************** Remove Set *********************

thisset = {"apple","banana","cherry"}
thisset.remove("banana")
print(thisset)

#Remove "banana" by using the discard() method:

thisset.remove("cherry")
print(thisset)


#Pop Set

thisset = {"apple","banana","cherry"}
x = thisset.pop()
print(x)

#Clear set

myset = thisset.clear()
print(myset)

#Del Set

thisset = {"apple", "banana", "cherry"}

del thisset

#print(thisset)

#*************************** Loop Set *********************************************

thisset = {"apple","Green Apple","Red Apple","Yellow Apple"}

for x in thisset:

    print(x)

#***************************Python - Join Sets *************************************

set1 = {"A","B","C"}
set2 = {1,2,3}

set3 = set1.union(set2)

print(set3)

#Use | to join two sets:

set4 = set1 | set2

print(set4)

#Join Multiple Sets

set1 = {"a","b","c"}
set2 = {1,2,3}
set3 = {"John","Elena"}
set4 = {"apple","banana","cherry"}

myset = set1.union(set2,set3,set4)
print(myset)
#When using the | operator, separate the sets with more | operators:

myset3 = set1 | set2 | set3 | set4

print(myset3)

#Join a Set and a Tuple

#The union() method allows you to join a set with other data types, like lists or tuples.

x = {"A","b","C"}
y = (1,2,3)

z = x.union(y)

print(z);


#The Update methods

set1 = {"A","B","C"}
set2 = {1,2,3}
set1.update(set2)
print(set1)

#Intersection

set1 = {"apple","banana","cherry"}
set2={"google","microsoft","apple"}

set3 = set1.intersection(set2)

print(set3)

#Use & to join two sets:

set1 = {"apple","banana","cherry"}
set2 = {"microsoft","google","apple"}

set3 = set1 & set2

print(set3)

#The intersection_update()

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}
set3 = set1.intersection_update(set2)


print(set1)

#The values True and 1 are considered the same value. The same goes for False and 0.

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection()

#the diffrence methods

set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set3 = set1.difference(set2)

print(set3)

#Use - to join two sets:

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3  = set1 - set2

print(set3)

#Use the difference_update() method to keep only the items from the first set that are not present in the other set:

set3 = set1 = {"apple","banana","cherry"}
set4 = set2 = {"google","microsoft","apple"}

set5 = set1.difference_update(set2)

print(set1)

#Symmetric update

set3 = set3.symmetric_difference(set4)


print(set3)

#You can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.

set1 = {"apple","banana","cherry"}
set2 = {"google","microsoft","apple"}

set3 = set1 ^ set2

print(set3)

#Use the symmetric_difference_update() method to keep the items that are not present in both sets:

set1 = {"apple","Mango","Cherry"}
set2 = {"google","microsoft","apple"}

set1.symmetric_difference_update(set2)

print(set1)


#Use the frozenset() constructor to create a frozenset from any iterable.

x = frozenset({"apple","banana","cherry"})

print(x)
print(type(x))