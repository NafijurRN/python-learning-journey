class Student :
    def __init__(self,name):
        self.name = name 
        
class CSEStudent(Student):  
    pass 
   
Student1 = CSEStudent("NAfij")

print(Student1.name)    