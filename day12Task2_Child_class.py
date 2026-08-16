class Person:
    def __init__(self,name):
        self.name =  name
        
class Student(Person):
    def __init__(self,name,department):
        super().__init__(name)
        self.department = department 
        
student1 = Student("Nafij","CSE")

print(student1.name)
print(student1.department)