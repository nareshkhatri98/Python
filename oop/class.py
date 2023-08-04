class Student:
    name = "Jhon"

    def show(self):
        print("hello")
        print(f"{self.name} is student")

obj = Student()
object
obj.show()



#apply arithmetic operation using class..

class Arithmetic:
    number1 =int(input("Enter the first number:"))
    number2 = int(input("Enter the second number:"))

    def add(self, number1,number2):   #self keyword is show the functions are exist in the class 
        sum = self.number1 + self.number2
        print("sume is :",sum)
    
    def subtract(self,number1,number2):
        sub = self.number1 - self.number2
        print("difference is : ",sub)
    
    def division(self, number1 ,number2):
        div =self.number1 / self.number2
        print("Division is :",div)

    def multiply(self, number1,number2):
        mul = self.number1 * self.number2
        print("multiplication is :",mul)

object =Arithmetic()

object.add(object.number1, object.number2)
object.subtract(object.number1, object.number2)
object.division(object.number1, object.number2)
object.multiply(object.number1, object.number2)