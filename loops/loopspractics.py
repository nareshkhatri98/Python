#create a list and print the even numbers only..
numbers = [1,2,3,4,5,6,7]
for i in numbers:
    if(i% 2 == 0):
     print("Even numbers are:",i)
    
# Prints out 0,1,2,3,4 and then it prints "count value reached 15"
print("-----Question 2-----")
count = 0
while(count<15):
   print(count)
   count += 1
else:
   print("count value reached %d " %(count))

for i in range(1,15):
   if(i%5 == 0):
      break;
   print(i)
else:
 print("This is not printed because for loop us terminated. because of break but not due t fail the condition")