class Person:
    def __init__(self,name):
        self.name=name
        
        
class Student(Person):
    def __init__(self,name,department):
        super().__init__(name)
        self.department = department
        
    def show_info(self):
        print("Name:",self.name)
        print("Department:",self.department)
        
        
student1 = Student("Nafij","CSE")
student1.show_info()
        