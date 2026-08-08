class Student:
    def __init__(self, name , marks):
        self.name = name 
        self.marks = marks
        
    
    def grade(self):
    
        if self.marks >= 80:
            return"A+"
        elif self.marks >= 70:
            return"A"
        elif self.marks >= 60:
            return"B"
        elif self.marks >= 50:
            return"C"
        else:
            return"F"
        
        
student1=Student("Nafij",75)

print("Student:",student1.name)
print("Grade:",student1.grade())

student2=Student("Rahim",45)

print("Student:",student2.name)
print("Student:",student2.grade())

    
       
        
   