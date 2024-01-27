# this is the example of the multilevel inheritance in python

class Shape():
    def show(self):
        print("this is the method of the shape class")
    def add(self):
        num1 = 13
        num2 = 12
        print("sum of the two number is", (num1+num2))
        
class Circle(Shape):
    def Display(self):
        print("this is the method of the circle class")
    def sub(self):
        num1 =2
        num2 = 1
        print("subtraction of the two number is", (num1-num2))
class Rectangle(Circle):
    def Demo(self):
        print("this is the method of the rectangel class")
    def Mul(self):
        num1 = 45
        num2= 100
        print("multiplication of the two number is", (num1*num2))

obj = Rectangle()
obj.show()  #this is the method of first parent class (Shape)
obj.add()
# calling the method of the class circle
obj.Display()
obj.sub()
# calling the method of the child class(Rectangle)
obj.Demo()
obj.Mul() 