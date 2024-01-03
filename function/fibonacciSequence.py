# To display the fibonacci sequence by using the recursive function.
# recursive function meas the function calling itself.
# Below the program.

def fibonacci(number):
  if(number<=1):
    return number
  else:
    return fibonacci(number-1) +fibonacci(number-2)
  
number = int(input("Enter the number do you want"))
if(number == 0):
  print("please enter a positive number.")
else:
   print(f"the  fibonacci sequence of the {number} is ")
   for i in range(number):
     print(fibonacci(i))
 
