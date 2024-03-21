name = "Naresh"
for i in name:
    print(i)



fullName = "Jhon Jhon"
for j in range(15):
    print(fullName)


#  create a multiply table in python
number = int(input("Enter the number do you want to calculate the multiplicatiion table: "))
for i in range(1,11):
    multi = number * i

    print(number, "*", i, "= ",multi )



number = int(input("Enter the row do you want"))
for i in range(1, number+1):
    for j in range(1, i+1):
        print("*", end="")
    print()


number1 = int(input("Enter the row do you want"))

for i in range(number, 0, -1):
    for j in range(0,i):
        print("*", end="")
    print()

