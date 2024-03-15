# methods that don't use the self parameter (work at class level)
# Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without ermanently modifying it.

class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age =  age
        self.address = address
    def Display(self):
        print(self.name, "is your name")
        print("Age is:",self.age)
        print("Address is:",self.address)

    @staticmethod
    def Hello():
        print("This is static method")

obj = Person("Jhon Jhon", 23, "UK")
obj.Display()        
obj.Hello()