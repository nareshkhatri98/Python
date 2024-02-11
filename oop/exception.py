# learn the exception handiling in python
# the exception handiling in python means to handle the unwanted errors occurs on our program that will be handled..
# example of the exception handiling....
def Multiplication():
    try:
     number = input("Enter the number: ")
     print(f"Multiplication table of {number}: ")

     for i in range(1,11):
        print(f"{int(number)} X {i}  = {int(number) * i} ")   
    except Exception as e:
     print(e)
  
Multiplication()


def DividedByZero():
  try:
    number = int(input("Enter the number do you want: "))
    result = number/0
    print("The result is: ",result)
  except Exception as e:
    print("Invalid opertion ",e)

DividedByZero()

def DemoFunction():
  try:
    list = [1,2,3,5,6,7,8]
    index = int(input("Enter the index: "))

    print(list[index])
  except Exception as e:
    print(e)
    # the code inside the finally block it is always executed...
  finally:
    print("I am always executed....")

DemoFunction()

# custom error(use the raise key word)

def function():
   salary = float(input("Enter the salary between 120000 and 300000: "))
   if( salary< 120000 or salary>300000):
     raise ValueError("The salary should be between 120000 and 3000000")
   print(salary)
      
function()