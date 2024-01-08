# create a two list x_list and y_list which contains 10 instance of x and y variables respectively. 
# also creat a list big_list which contains variable x and y , 10 times  each by concatenating  the two list.


x = object() 
y = object()


x_list = [x] * 10
y_list = [y] * 10

big_list = x_list + y_list

print("the length of the list x is: ", len(x_list))

print("the length of the list y is: ", len(y_list))

print("the length of the  big list is: ", len(big_list))
 
if x_list.count(x) == 10 and y_list.count(y) == 10 :
  print("the both list contains the same length")

if big_list.count(x) == 10 and y_list.count(y) == 10 :
  print("also the big list contains the same length!") 
