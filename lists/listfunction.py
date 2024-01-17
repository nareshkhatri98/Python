my_list = [13,4,5,6,7,8,9,10,11,21,12,14,141,45]

print(my_list)

# len(): the len() function is used to find out the length of the list.
print(len(my_list))

# max() : the max() function is used to  find out the largest element in the list.

print(max(my_list))

# min() : the min() function is used to find out the smallest element in the list.

print(min(my_list))

# list(anyy vraibes) : it converts the list
s = range( 1, 17)
print((list(s)))

print(sum(my_list))

# for loop in list

Numbers = [0,1,2,3,4,5,6,7,8,9]
for element in Numbers:
    if(element% 2 ==1):
        print(element)

for element in Numbers:
    print(element **2, end =" ")