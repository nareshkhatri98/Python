list =[11,1,2,4,5,7,8,9,12,15,0,10]
print(list)

#List manipulation functions..
list.append(100)# the append method is used add the new items at the end of the list.
print(list)

#negative indexing
print(list[-10])
print(list[len(list)-10])

#To chech the element is exist or not on the list.

if 13 in list:
    print("yes")
else:
    print("No")
  
if len(list) == 2:
    print("yes")
else:
    print("No")

#jump index: This methos helps to jmup one index to anther index
print(list[0:9]) # this line show this is item form ixed 0-9
print(list[0:9:4]) # this line show the item when index jump by 4.

#list Compreshesions: this statements is used  for creating a new list from other iterable like list, tuples sets etc.
# example 
color = [i for i in range(12)]

print(color)
color2 = [j*j for j in range(12) if j%2==0]
print(color2)

#sort()this methods  returs the items in ascending order
list.sort()
print(list)
list.sort(reverse=True) # this line retuns the items in descending order
print(list)

#reverse() this method retuns the items in reverse order of the inintial list of items

list.reverse()
print(list)

#copy()
demo =list.copy()
demo[0] = 10000
print(demo)

# insert() this method is used for insering the items on the basis of the index

color = ['red', 'yello','green']
color.insert(3,"aa")
print(color)

characteres =['a','b','c','d','e', 'f','g']
numbers =[1,2,3,4,5,6,7]
#characteres.insert( 1, numbers)
#print(characteres)


# extend() this methos is used for adds the an entire list of items S
characteres = characteres +list
print(characteres)