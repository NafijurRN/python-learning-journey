class Person:
    def __init__(self,name):
        self.name = name 
        
class Student(Person):
  pass


student1 = Student("Nafij")
print(student1.name)        