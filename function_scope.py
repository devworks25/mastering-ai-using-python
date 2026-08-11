#Scope
#A variable is only available from inside the region it is created. This is called scope.

#Local Scope
#A variable created inside a function belongs to the local scope of that function, and can only be used inside that function.

x=500
def myfunction():
    x=300
    print(x)

myfunction();

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()

x=500

def myFunctionGlobal():
   print(x)

myFunctionGlobal()

print(x)

y=600
def myFunctionGlobalLocal():
   y=200
   print(y)

myFunctionGlobalLocal()
print(y)


#Global Keyword function

x=560
def myGlobalvar():
   global x
   x = 700

myGlobalvar()
print(x)

#No Local var

def myNonLocalVar():
   x = "Jane"

   def myNonLocalVar2():
      nonlocal x
      x = "Hello"
   myNonLocalVar2()
   return x

print(myNonLocalVar())


##The LEGB Rule
#Python follows the LEGB rule when looking up variable names, and searches for them in this order:

#Local - Inside the current function
##Enclosing - Inside enclosing functions (from inner to outer)
#Global - At the top level of the module
#Built-in - In Python's built-in namespace

x = "global"

def outer():
   x = "enclosing"

   def inner():
      x ="local"
      print("Inner",x)
   inner()
   print("Outer",x)

outer()
print("Global",x)