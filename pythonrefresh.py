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
print("Hi",name)



