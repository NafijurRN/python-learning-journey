class student:
    def __init__(self, name, age, department):
       self.name = name 
       self.age = age
       self.department =department 
    
    def show_info(self):
      print("My name is",self.name)
      print("I am ",self.age,"years old")
      print("My department is",self.department)
    
student1=student("Shihab",18,"Civil")
student1.show_info()

student2=student("Siam",20,"EEE")
student2.show_info()
    
