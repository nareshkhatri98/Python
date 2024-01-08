# this  print out Hello, Ram!.

name  = "Ram"
print("Hello, %s!" %name)

#this print out  "ram is 23 years old."

name = 'ram'
age = 23

print("%s is %d  years old. " %(name, age))

# this print out : A list :[2,3,4]

mylist = [2,3,4]

print("A list : %s" %mylist)

# Exercise:

# QN  You will need to write a format string which prints out the data using the following syntax: 
# Hello Ram Thapa. Your current balance is $53.44. 

data = ("Ram", "Thapa", 53.44)

formating_string = "Hello %s %s. your current balance is $%s."

print(formating_string  %data)

