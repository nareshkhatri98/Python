# inheritance means the child class access the properties,method behaviours of the parent class
# This is an example of the single level inheritance hierarchy..
class Person:
      def __init__(self, name, age, email, address):
            self.name = name
            self.age = age
            self.email = email
            self.address = address

      def add(self,num1,Num2):
            sum = num1 +Num2
            print(sum)
      def show(self):
            print("this is the Parent class method")

            #--- inheritate the parent class by ht  
class Demo(Person):
      
      def __init__(self, name, age, email, address, phone):
                  self.name = name
                  self.age = age
                  self.email = email
                  self.address = address
                  self.phone = phone

                  Person.__init__(self, name, age, email, address)
            
      def details(self):
            print("Name is: ",self.name)
            print("Age is: ", self.age)
            print("Email is: ",self.email)
            print("Address is: ", self.address)
            print("phone is: ",self.phone)
      def Sub(self,num1, Num2):
            sub= num1 - Num2
            print(sub)

obj = Demo("Naresh", 21, "naresh@gmail.com","KTM", 9810068245)
obj.details()
obj.Sub(13,12)
obj.add(13,12)
obj.show()
