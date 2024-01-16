my_list = [12, 14, "Ram", 4, 8, 9]
print(my_list)
# append : this method is used to add the new items in list which will be added to the end of the list.
my_list.append(12)
print(my_list)

#  insert : this method is used to add the new items at the specified position in the list.

my_list.insert(1, 13)
print(my_list)

# pop : this mehtod is used to remove the items from the list.
my_list.pop(0)
print(my_list)

# remove : this method is used to remove the specified item form the lsit.
my_list.remove(13)
print(my_list)


new_list = [12,14,151,7,8,9,0,12]
# reverse : the reverse method is used to reverse the items in the list.
new_list.reverse()
print(new_list)

# sort :the sort method is used to sort the items in  the list.
new_list.sort()
print(new_list)

# index : the index method is used to find out the index of the item in the list.
print(new_list.index(151))

# count : the count method is used to count the particular items how many times present in the list.

print(new_list.count(12))
# clear : the clear method is used to clear the list.
print(new_list.clear())
