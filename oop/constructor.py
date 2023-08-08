#constructor in python...


class Test:
    name =str(input("Eente yput name:\n"))
    age =int(input("Enter your age:\n"))
    position= str(input("Enter your position:\n"))
    def __init__(self):
      self.name  
      self.age 
      self.position 
    
    def show(self):
        print("your  name is  " +self.name +", age is "+str(self.age) +" And opistion is "+self.position +".")

object = Test()

object.show()

#Parametrize constructor
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)

# Creating objects using the parameterized constructor
person1 = Person("Ram", 25)
person2 = Person("jam", 30)

# Displaying the information using the display method
person1.display()
person2.display()
