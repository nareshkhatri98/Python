def factrioal() :
  num = int(input("Enter the number::"))
  factrioal =1
  if(num<0):
    return "not possible"
  
  elif(num == 0):
     return "factrioal is 1"
  
  else:
    for i in range(1 ,num +1):
      factrioal = factrioal * i
    return factrioal
    
result = factrioal()
print("factrioal is", result)
