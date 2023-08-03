name ="Naresh"
for i in name:
    print(i)


for i in range(8):
    print(i)


#multiplicity table in python

number = int(input("Enter a number do you want to multiply:"))

for i in range(1,11):
    print(number, "*",i,"=",number*i)



#pattern questions in python
''''
*
**
***
****
*****
'''

for i in range(5):
    for j in range(i+1):
      print("*", end="")
    print()

for i in range(5):
    for j in range(i+1):
        print("*", end="")
    print()
