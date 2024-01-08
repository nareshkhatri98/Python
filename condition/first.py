x = 7
print(x==2)
print(x==7)
print(x<7)

# bolean operators.

name = "ram"
age = 30
if name == "ram" and age == 30 :
  print("your name is %s and  age is %d" %(name, age))

if name == "Hari " or age == 23 :
  print("your name is  Hari and age is 23")



number = 15
first_array = [2,3,4,5]
second_array =[7,8,9]

if number > 14:
  print("true")
if first_array[0] >1 and first_array[3] >= 5:
  print("true")
if second_array[0]>6 or second_array[2]<8 :
  print("true")