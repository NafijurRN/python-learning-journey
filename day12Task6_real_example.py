class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
class Developer(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language = language
        
    def show_info(self):
        print("Name:",self.name)
        print("Salary:",self.salary)
        print("language:",self.language)
        
        
employee1 = Developer("Nafij",30000,"Python")
employee1.show_info()
        
        