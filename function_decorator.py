Function Decorator

# #Basic Decorator

import functools
# def changecase(func):
#     def myinner():
#         return func().upper()
#     return  myinner

# @changecase
# def changecase_function():
#     return "Hello Sally " 

# @changecase
# def other_function():
#     return "I am speed"
 
# print(changecase_function())
# print(other_function())

# #Arguments in the Decorated Function

# def change_case_arg(func):
#     def myinner(x):
#         return func(x).upper()
#     return myinner

# @change_case_arg

# def myfunction2(nam):

#     return  "Hello Sally " + nam


# print(myfunction2("John"))


# #*args and **kwargs

# def change_upper_case(func):
#     def myinner(*args , **kwargs):
#         return func(*args,**kwargs).upper()
#     return  myinner

# @change_upper_case
# def myfunction3(nam):
#     return "Hello" + nam

# print(myfunction3("John"))

#Decorator With Arguments
def my_change_case_with_arg(n):
  def changecase(func):
    def myinner():
      if n == 1:
        a = func().lower()
      else:
        a = func().upper()
      return a
    return myinner
  return changecase

@my_change_case_with_arg(2)
def myfunction4():
  return "Hello Linus"

print(myfunction4())


#Multiple Decorators

def changecase_5(func):
  def myinner():
    return func().upper()
  return myinner

def addgreeting(func):
  def myinner():
    return "Hello " + func() + "Have a good day !"
  return myinner

@changecase_5
@addgreeting
def myfunction5():
    return "Tobias"
print(myfunction5())

#Preserving Function Metadata
@changecase_5
def myfunction6():
  return "Have a great day !"
print(myfunction6.__name__ )

#functools.wraps
def changecase_7(func):
  @functools.wraps(func)
  def myinner():
    return func().upper()
  return myinner

@changecase_7
def mydemofunction():
  return "Have a Nice Day ++"

print(mydemofunction.__name__)
