class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        
    def show_info(self):
           print("Name:",self.name)
           print("Salary:",self.salary)
           
class Developer(Employee):
    def __init__(self, name, salary,language):
        super().__init__(name, salary)
        self.language = language
        
    def show_info(self):
        super().show_info()
        print("Language",self.language)
        
developer1 = Developer("Nafij",   30000,  "Python")
developer1.show_info()
        

        