class Person:
    def introduce(self):
        print("I am Nafij")

class Student(Person):
    def introduce(self):
        super().introduce()
        print("I am a CSE Student")
        print("Department:CSE")
        
        
student1 = Student()
student1.introduce()