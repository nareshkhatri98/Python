# learn the exception handiling in python
# the exception handiling in python means to handle the unwanted errors occurs on our program that will be handled..
# example of the exception handiling....
def Multiplication():
    try:
     number = input("Enter the number")
     print(f"Multiplication table of {number}: ")

     for i in range(1,11):
        print(f"{int(number)} X {i}  = {int(number) * i} ")   
    except Exception as e:
     print(e)
  
Multiplication()


def DividedByZero():
  try:
    number = int(input("Enter the number do you want"))
    result = number/0
    print("The result is: ",result)
  except Exception as e:
    print("Invalid opertion ",e)

DividedByZero()