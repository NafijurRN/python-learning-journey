class Student:
    def show_name(self):
        print("I am a student")
        
class CSEStudent(Student):
    pass

student1 = CSEStudent()
student1.show_name()
    