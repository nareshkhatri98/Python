# create student class that takes name and marks of 3 subjects as arguments in constructor.
# Then create a method to print the average.

class Student:
    def __init__(self, name ,marks):
        self.name = name
        self.marks = marks
    
    def Average(self):
        sum = 0
        for i in self.marks:
            sum += i

        print(sum)
        average = sum /3
        print("hi", self.name, "Your average score is:", average)

obj = Student("Narresh", [45,56,45])
obj.Average()
