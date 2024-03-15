# Hiding the implementation details of a class and only showing the essential features to the user...
class Car:
    def __init__(self):
        self.accelerate = False
        self.Break = False
        self.Clutch = False

    def start(self):
        self.Clutch = True
        self.accelerate = True
        print("Car is started......")

car1 = Car()
car1.start() 