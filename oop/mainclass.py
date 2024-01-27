# learn the oop in python..
# create a class using the class keyword.........
class Person:
    name = "Naresh Khatri"
    occupation = "Python Developer"
    Address = "Kathmandu"
 # create a method using the def keyword.........
    def show(self):
        print(self.name)
        print(self.occupation) 
        print(self.Address)
     # to print the all information in one line,...
        print(f"{self.name} is a {self.occupation} and the lives in {self.Address}")  
# creating  the object of the class Person....
obj = Person()
obj.show() 
#  class that contains the all arithmetic operations....
class Arithmetic:
      
      def __init__(self, Number1, Number2):
         self.Number1 = Number1
         self.Number2 = Number2

      def Add(self):
         return self.Number1 + self.Number2

      def Sub(self):
         return self.Number1 - self.Number2 
     
      def Mul(self):
         return self.Number1 * self.Number2
     
      def Div(self):
         return self.Number1 / self.Number2
     
      def Mod(self):
         return self.Number1 % self.Number2

# --- creating objects----   
      
obj1 = Arithmetic(12,10)
print("Addition is: " ,(obj1.Add()))
print("Subtraction is: " ,(obj1.Sub()))
print("Multiplication is:" ,(obj1.Mul()))
print("Division is: " ,(obj1.Div()))
print("Modulus is: " ,(obj1.Mod()))
    
# exmple-3
class Person:
     FullName ="Naresh"
     def __init__(self, Name,Id):
         self.Name = Name
         self.Id = Id
   
     def show(self):
         print("Name of the person is:",(self.Name))
         print("Id of the person is:",(self.Id))

obj2= Person("Naresh", 12)
obj2.show()