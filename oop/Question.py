# create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def Average(self):
        sum = 0
        for i in self.marks:
            sum += i

        print(self.name, "yor average marks in  the three subject is: ", (sum/3))

obj = Student("Naresh", [12,13,14])
# print(obj.name, obj.marks)
obj.Average()