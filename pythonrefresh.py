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
name = input("Enter your name?")
#print("Hi",name)

#Lists, tuples and sets
l  = ["Mohd", "Mudathir", "ALi"] # can be changed, maintain order & allow duplicates
t  = ("Mohd", "Mudathir", "ALi") # can not be changed, maintain order & allow duplicates
s  = {"Mohd", "Mudathir", "ALi"} # can be changed, doesn't maintain order & doesn't allow duplicates

l.append("mahi") # can't add to tuble
s.add("mahi")

#Advanced set operations difference, union and intersection
art = {"Ahmed", "Jon", "Lily", "Han"}
science = {"Khalid", "Omer" "Jon", "Lily", "Han"}
dif  = art.difference(science)
all  = art.union(science)
both = art.intersection(science)
print(dif)
print(all)
print(both)