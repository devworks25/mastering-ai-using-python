#Python - Access Dictionary Items


#Accessing Dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

print(thisdict["model"])


#use get method for getting dist

x = thisdict.get("brand")
print(x)


#Get keys of 

x = thisdict.keys()

print(x)

#Update keys 

thisdict['brand'] = "Hyundai"

print(thisdict)


#Get value of dict

print(thisdict.values())

#Get itesm o disct

items = thisdict.items()

print(items)

#check if item exist in dict

if "model" in thisdict and thisdict["model"] == "Mustang":
    print("Yes model exists")


#change item

thisdict["model"] = "KIA"
print(thisdict)

#Update dict

thisdict.update({"model":"Neo"})

print(thisdict)

#Add items to dict

thisdict['color'] = "red"

print(thisdict)

#Update new key value in dict

thisdict.update({"RIM":"Steel"})

print(thisdict)

#Remove item from dict

thisdict.pop("model")

print(thisdict)

#Pop item

thisdict.popitem()

print(thisdict)


#use del key

del thisdict['color']

print(thisdict)

#Use clear

thisdict.clear()

print(thisdict)



#Loop Dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

for x in thisdict:
    print("Print Key: " + x)
    print("Print Value: " + str(thisdict[x]))


#Print Values only

for x in thisdict.values() :

    print(x)

#Print Keys only

for x in thisdict.keys():
    print(x)


#Loop through both keys and values, by using the items() method:

for x,y in thisdict.items():

    print(x,y)


#Copy a dict

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

mydict = thisdict.copy()

print(mydict)

#Another way to make a copy is to use the built-in function dict().

mydict = dict(thisdict)
print(mydict)

#Python - Nested Dictionaries


myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily)

#Nested dict

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}

print(myfamily)

#Access Items in Nested Dictionaries
 
print(myfamily["child1"]["year"])

#Loop Through Nested Dictionaries

myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x, obj in myfamily.items():
    print(x)
    
    for y in obj:
        print(y + ':', obj[y])