class Naresh:
    def __init__(self,Name, age, phone, address):
        self.Name = Name
        self.age = age
        self.phone = phone
        self.address = address
    def show(self):
        print("Name is: ", self.Name)
        print("Age is : ",self.age)
        print("Phone is :",self.phone)
        print("Address is :", self.address)

class Demo(Naresh):
    # calling the parent constructor
    def __init__(self,Name,age, phone,address, eductaion, Department):
        self.education = eductaion
        self.Department = Department
        Naresh.__init__(self, Name, age, phone, address)

    def Display(self):   
     
        print("Eduction is :",self.education)
        print("your Department is :",self.Department)
     


obj = Demo("Naresh Khatri", 21, 9844703218, "Kathmandu", "BCA 5th sem", "Humanities" )
obj.show()
obj.Display()


        