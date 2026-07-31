students = []

while True:
    print("\n=================Student Management System======================")
    print("1.Add Student")
    print("2.View Students")
    print("3.Remove Student")
    print("4.Exit")
    
    choice = input("Enter your choice: ")
    if choice == "1":
        student = input("Enter student name: ")
        students.append(student)
        print("Student added Successfully.")
        
    elif choice == "2":
        print("\nStudent List: ")
        
        for student in students:
            print(student)
            
    elif choice == "3":
        student = input("Enter student name to remove : ")
        
        if student in students:
            students.remove(student)
            print("Student Removed Successfully.")
        else:
            print("Student not Found")
       
        