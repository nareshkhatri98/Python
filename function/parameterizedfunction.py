# parameterized / Argumented function: the functio which takes the arguments during the initialization  process is called
# the parameterized function. Below the example of the parameterized function without retrn types.

def Addition( number1, number2):
  sum = number1+ number2
  print(f" the sum of the two numbers {number1} and {number2} is: {sum}")

def Subtract(number1, number2):
  subtract = number1 - number2
  print(f"the difference of the two numbers {number1} and {number2} is : {subtract}")

def Multiply(number1 ,number2):
  Multiply = number1 * number2
  print(f"the multiplication of the two numbers {number1} and {number2} is: {Multiply}")

def Division(number1, number2):
  Divide = number1 / number2
  print(f"The dividion of the two numbers {number1} and {number2} is: {Divide}")

def Mode(number1, number2):
  mode = number1 % number2
  print(f"the mode is {mode}")

#calling the all above funtion..
Addition(12,3)
Subtract(13,2)
Multiply(12,2)
Division(14,7)
Mode(15,4)
  