print(10 > 9)
print(10 == 9)
print(10 < 9)

#Boolean Values in conditions
a = 200
b = 33
if b > a:
  print("b is greater than a")


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

#Evaluate Values and Variables
print(bool("Hello"))
print(bool(15))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))