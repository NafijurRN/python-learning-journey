class Person:
    def introduce(self):
        print("I am a Person")
        
class Student(Person):
    
    def introduce(self):
        print("I am a CSE student")
    
student1 = Student()
student1.introduce()