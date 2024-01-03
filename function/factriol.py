number = int(input("Enter the number do you want to find the factrioal."))
def findfactrioal():
  
  factrioal =1
  if(number<0):
    print("Factrioal is not possible")
  elif(number == 0) :
    print("Factrioal is 1.")
  else:
    for i in range(1, number): 
     factrioal = factrioal*i
    return factrioal
  
Result = findfactrioal()
print(f"The factorial of {number} is: {Result}")

