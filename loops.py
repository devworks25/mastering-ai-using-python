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

