#creating function ..
# to create function we can use def key word.
def FindPrime():
  number = int(input("Enter a number:"))
  count = 0
  for i in range(1, number+1):
    if(number%i == 0):
      count +=1
 
  if(count == 2):
   print(f"the {number} is prime.")
  elif(count > 2):
    print(f"The {number} is composite.")
  else:
    print(f"the {number } is either prime or not composite.")
    
FindPrime() #calling function..