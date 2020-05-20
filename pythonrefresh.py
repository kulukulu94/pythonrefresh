#intergers, floats
x = 15
price = 9.99
discount = 0.2 
result = price * (1 - discount)
#print(result)

#strings
name = "Ali"
#print(name * 2 ) #this basicly means AliAli

#changing variable value
a = 25 
b = a
#print(a)
#print(b)
b = 17
#print(a)
#print(b)

#String formating in python using f string
name = "Bob"
greeting = f"Hello, {name}"
#print(greeting)
#or
name = "Jon"
#print(f"Hello, {name}")
#formatted
longer_phrase = "Hello, {}. Today is {}"
formatted = longer_phrase.format("Mohammed", "Wednesday")
#print(formatted)

#Getting User Input
#name = input("Enter your name?")
#print("Hi",name)

#Lists, tuples and sets
l  = ["Mohd", "Mudathir", "ALi"] # can be changed, maintain order & allow duplicates
t  = ("Mohd", "Mudathir", "ALi") # can not be changed, maintain order & allow duplicates
my_tuple = 15, #this is a single value tuble
s  = {"Mohd", "Mudathir", "ALi"} # can be changed, doesn't maintain order & doesn't allow duplicates

l.append("mahi") # can't add to tuble
s.add("mahi")

#Advanced set operations difference, union and intersection
art = {"Ahmed", "Jon", "Lily", "Han"}
science = {"Khalid", "Omer" "Jon", "Lily", "Han"}
dif  = art.difference(science)
all  = art.union(science)
both = art.intersection(science)
#print(dif)
#print(all)
#print(both)

#booleans in python
#print(5==5)
#print(5 > 5)
#print(10 != 10)
# comparisons: ==, !=, >, <, >=, <=

#is key word checks if the elements are exactly the same thing not ust they have the same elements/values

#if statements 
''' 
day_of_week = input("what day of the week is it today?").lower()

if day_of_week == "monday":
    print("Have a great start to your week!")
elif day_of_week == "tuesday":
    print("It's Tuesday")
else:
    print("Full speed ahead!")
    
# in keyword works in lists, tuples, sets and strings

watched_movies = {"The Matrix", "Green Book", "Her"}    
user_movie = input("Enter something you have watched recently: ")

print( user_movie in watched_movies)

#if statement with in keyword
watched_movies = {"The Matrix", "Green Book", "Her"}    
user_movie = input("Enter something you have watched recently: ")

if user_movie in watched_movies:
    print(f"I have watched {user_movie} too!")
else:
    print("I have not watched that yet!")    
      '''
####
''' number = 7
user_input = input("Enter 'y' if you would like to play: ").lower()

if user_input == 'y':#it can be user in ("y", "Y")
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly")
    elif abs(number - user_number) == 1:#can be (number - user_number) in (1, -1)
        print("You were off by one.")
    else:
        print("sorry, it's wrong!")      
 '''
##loops while, 
''' 

while True:
    number = 10
    user_input = input("Enter 'y' if you would like to play? (Y/n): ")#Y/n common naming convention
    
    if user_input == "n":
        break
    
    user_number = int(input("Guess our number: "))
    if user_number == number:
        print("You guessed correctly")
    elif abs(number - user_number) == 1:#can be (number - user_number) in (1, -1)
        print("You were off by one.")
    else:
        print("sorry, it's wrong!")      
         '''

''' ##loops, for
friends = ["Rolf", "Jon", "Bon"]

for friend in friends:
    print (f"{friend} is my friend.")
   '''  
''' #sum, len
grades = [25,54, 66, 77]
total  = sum(grades)
amount  = len(grades)
print(total/amount)   
 '''
''' ##list comprehension
friends = ["Rolf", "Sam", "Samantha", "sony", "Jon"]
starts_s = [friend for friend in friends if friend.startswith("S") ]
print(starts_s)

 '''
""" ## dictionaries python dictionaries similar to php associative arrays
student_attendance = {"Jon": 90, "Elly":30, "Mark": 44}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
    
attendance_values =student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
 """
""" ##estructuring variables
x = 5, 11 #it's a tuble not nessecarly to have ()

x, y = 5, 11 # better than assigning vales separately

t = 5, 11
x, y = t

print(x, y)# python is smart enought to get that from t

# for student, attendance in student_attendance.items(): this splitng is called destructuring

head, *tail = [1, 2, 3, 4, 5] # head = 1 , *tail =the rest
*head, tail = [1, 2, 3, 4, 5] # *head = [1, 2, 3, 4]  , tail =the last 5
 """

""" ##Functions
def hello():
    print(hello)

hello()# calls the function
#age calculator function
 """
# u can't reuse function's name inside it for variables

#concept of global and local variable within the function

# u cant call fuction before its defined


""" ##Functions Arguments and parameters
def add(x,y):
    pass # means do nothing
#u cant put positonal argumeent after named argument add(x=5, 6)
#you cant pass positional arguments to a function that doesn't have parameters
#to be cont....
 """
##Default parameter Values
""" def add(x, y=7):
    print(x + y)# y is optional one argument can be passed as y default
     """
#u cant have def add(x=5, y)

#when function encounter return it wil terminate and ingore rest of lines

##Lambda functions
""" 
add = lambda x, y: x+y
print((lambda x, y: x+y)(5, 7))


def double():
    return x * 2

sequence =[1, 3, 5, 9]

doubled = [double(x) for x in sequence]
#instead can be
doubled =map(double, sequence)# applies each of seq. to double func.
 """
""" #using lambda
sequence =[1, 3, 5, 9]
#doubled = [(lambda x: x * 2)(x) for x in sequence]
doubled =list(map(lambda x: x * 2, sequence))# 
print(doubled)

 """
""" ##dictionary comprehensions
users = [
    (0,"Jon", "Password"),
    (1, "Khalid", "3rrsdfdsaf"),
    (2,"Jame", "wordx"),
    (3, "Khan", "000f")
]

username_mapping = {user[1]: user for user in users}
print(username_mapping)
 """
""" ##unpacking argument  this is awy of collecting multiple arguments into a single papameter
def multiply(*args):# this means a set of arguments will be collected into a tuple of arguments
    print(args)
    for arg in args:
        total = total * arg

    return total

print(multiply(1, 3, 5))

#destructuring one argument into multiple parameters
def add(x, y):
    return x + y

nums = [3, 5]
add(*nums)#this destructs them its the opposite of the above
nums = {"x": 15,"y": 25}
add(**nums)#in case of a dictionary this will take the values of the dic. keys that are exact as papameters names any pass them to each parameter
#good practise to use same params names as dic keys to simplify the code


def apply(*args, operator):
    if operator == "*":
        return multiply(args)#there is a bug as args r collected as tuple better to user multiply(*args) which upack them
    elif operator == "+":
        return sum(args)
    else:
        return "No valid operator provided to apply()."
    
    print(1, 4, 5, 6, operator="+")
   """  
    
""" ##unpacking keywords arguments

def named(**kwargs):#this function collects named arguments into a dictionary where dic. keys = names of args
    print(kwargs)
    
named(name="bob", age=25)    

#the opposite of above upack a dict, into named args
def named(name, age):
    print(name, age)
    
details = {"name": "Mohammed", "age": 25}

named(**details)

#nicely function...

#doing both *args, ***args, **kwargs ,kwargs=keyword arguments

def both (*args, **kwargs):
    print(args)
    print(kwargs)
    
print(1, 3, 6, name="Mohd", age= 25) #positional arguments"1, 3, 6, " while be collected into args and named argument "name="Mohd", age= 25" will be collected into kwargs
  """
##OOP in Python

""" class Student:
    def __init__(self):#a function inside class is called method
        self.name = "Rolf"
        self.grades = (30, 60, 40, 44,)
        
    def average(self):
        return sum(self.grades)/len(self.grades)
    
student = Student()#the object is created by __init__ method
print(Student.average(student))
 """
#to be cont...
        
        
##Magic methods __str__ & __repr__


##@classmethod and @staticmethod

#to be cont...
#use if u want a method that does not use the class or the instance use static
#use if u want a method that use the class use classmethod
#use if u want a method that use the object/instance/self then use the instance method


##Class inhertance

#....

##Composition

#.....

##Type hinting in python 3.5+

from typing import List

def list_avg(sequence) :
    return sum(sequence) / len(sequence)


list_avg([1, 3, 6])