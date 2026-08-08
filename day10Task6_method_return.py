class Student:
    def __init__(self, name, math, english):
        self.name = name
        self.math = math
        self.english = english
        
    def total_marks(self):
        return(self.math + self.english)


student1=Student("Siam",20,30)
print(student1.total_marks())

    