# python dictionary is an unordered collection of items. while other compound  data types have only value as an element  a dictionary has a key : vlaue pair

Marks = {'Ram':45, "Hari": 56, "Bisham": 59}
print(Marks)

print(Marks["Hari"])


Squares = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
for element in Squares:
    print(element, Squares[element])



# Updating the  Dictionary items

My_dict = {'name': 'Naresh', 'age': 20}
print(My_dict)

# update the age
My_dict['age'] = 30
print("upadated age is:")
print(My_dict)


print(My_dict.pop('name'))
print(My_dict)


