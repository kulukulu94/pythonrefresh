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
#loops while, 
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

''' #loops, for
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
''' #list comprehension
friends = ["Rolf", "Sam", "Samantha", "sony", "Jon"]
starts_s = [friend for friend in friends if friend.startswith("S") ]
print(starts_s)

 '''
# dictionaries python dictionaries similar to php associative arrays
student_attendance = {"Jon": 90, "Elly":30, "Mark": 44}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")
    
attendance_values =student_attendance.values()
print(sum(attendance_values) / len(attendance_values))
