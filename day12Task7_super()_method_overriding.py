class Employee:
    def show_role(self):
        print("I am a Employee")
        
class Developer(Employee):
    def show_role(self):
        super().show_role()
        print("I am a Developer")
        
developer1= Developer()
developer1.show_role()