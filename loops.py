#Loops

#Basic For Loop

fruits = ['apple','banana','cherry']

for x in fruits:
    print(x)

#Loops by string

hello = 'hello world'
for x in hello:
    print(x)    

#Break Statment
number = [1,2,3,4,5,6,7,8,9] 
for x in  number:
    print(x)
    if x == 5:
        break   

for x in fruits:
    if(x=='banana'):
        break
    print(x)    


#continue statement

for x in fruits:
    if(x=='applee'):
        continue
    print(x)    

#Range Function

for x in range(6):
    print(x)    

for x in range(2,6):
    print(x)

for  x in range(2,30,6):
    print("New Range\n")
    print(x)

for a in range(8):
    print(a)
else:
    print("Finally Finshed")

#Break Loop when x is 3

for x in range(10):
    if(x==3):break
    print(x)
else:
    print("Finally Finished")

#Nested Loops
adj=['red','big','tasty']
fruits=["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

#The Pass Statement
for x in [0,1,2]:
    pass


# /*********************************************Do While Loops****************************************/

print("While loop start")

i = 1
while i <= 6:
    print(i)
    i += 1  

#Break Statement
i = 1
while i < 6:
    print(i)
    if i ==3:
        break
    i +=1

#The Continue statement

i = 0
while i < 6:
    i+=1
    if(i==3):
        continue
    print("hellp", i)

i=1
while i < 6:
    print(i)
    i +=1
else:
    print("I m done")

fruits = ["apple","banana","cherry"]

#Print each fruit in a fruit list:
for x in fruits:
    print(x)

#Loop through the letter in the word "banana"
for x in "banana":
    print(x)

#Exit the loop when x is banana:

fruits = ["apple","banana","cherry"]

for x in fruits:
    print(x)
    if x == "banana":
        break


# Exit the loop when x is "banana", but this time the break comes before the print:
fruits = ["apple","banana","cherry"]

for x in fruits:
    if x == "banana":
        break
    print(x)


# The continue statement we can stop the current

for x in fruits:
    if x == "banana":
        continue
    print(x)

# The Range function

for x in range(6):
    print(x)

for y in range(2,10):
    print(y)

#Increment sequence with default 3

for x in range( 2, 30 , 3):
    print(x)
else:
    print("Job has been done")


#With else break,range

for abc in range (2,40,2):
    
    if abc % 2 == 0:
        print("Even Number ", abc)
        continue
    else:
        break

# nested Loops

adj = ["red","big","tasty"]
fruits = ["apple","banana","cherry"]

for x in adj:
    for y in fruits:
        print(x,y)

#The pass

for x in [0,1,2]:
    pass