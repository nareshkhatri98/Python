# f = open('data.txt', 'r')

# for line in f:
#     print(line)

# f.close()

# with the help of the "with" keyword we there no required to close the file.

# with open("write_data.txt", 'w') as file:
#     age = input("Enter the age") 
#     file.write(age)
    

with open("write_data.txt", 'r') as file:
     content = file.readline()
     print("your age is ",content)


