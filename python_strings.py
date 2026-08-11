#Quotes Inside Quotes
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

#Assign String to a Variable

a = "Hello"
print(a)

#Multiline Strings

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""
print(a)

#three single quotes:
a = '''Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua.'''
print(a)

#Strings are Arrays
a = "Hello, World!"
print(a[1])

#Looping Through a String
for x in "banana":
  print(x)  

#String Length      
a = "Hello, World!"
print(len(a))

#Check String
txt = "The best things in life are free!"
print("free" in txt)

#Print only if "free" is presen

if "free" in txt:
  print("Yes, 'free' is present.")      

#Check if NOT
txt = "The best things in life are free!"   
if "free" not in txt:
  print("No, 'free' is NOT present.")

  txt = "The best things in life are free!"
if "expensive" not in txt:
  print("No, 'expensive' is NOT present.")


  #String Concatenation
  a = "Hello"
  b = "World"
  c = a + b
  print(c)

  #To add a space between them, add a " ":  
  a = "Hello"
  b = "World"
  c = a + " " + b
  print(c)

  #String Format
  age = 36
  txt = "My name is John, and I am {}"
  print(txt.format(age))

  #F-Strings
  age = 36
  txt = f"My name is John, and I am {age}"
  print(txt)  

  #Add a placeholder for the price variable:  
  price = 49.99
  txt = f"The price is {price} dollars"
  print(txt)

  #Display the price with 2 decimals:

  price = 59
  txt = f"The price is {price:.2f} dollars"
  print(txt)

  txt = f"The price is {20 * 59} dollars"
  print(txt)

  #Evalulate Values in Strings
  x = "Hello"
  y = 15

  print(bool(x))
  print(bool(y))

  #More Bool

  bool("abc")
  bool(123)
  bool(["apple", "cherry", "banana"])

  class myclass():
    def __len__(self):
      return 0

  myobj = myclass()
  print(bool(myobj))