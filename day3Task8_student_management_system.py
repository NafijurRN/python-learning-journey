students=[]

print("==============Student Managemet System================")
print("1.Add Student")
print("2.View Students")
print("3.Remove Student")

choice = input("Enter yours choice:")
print("Your Choice is :",choice)

if choice =="1":
    students_name = input("Enter student name:")
    students.append(students_name)
    print("Student added successfully")
    
elif choice =="2":
    print("Students",students)
    
elif choice =="3":
    students_name =input("Enter student name to remove: ")
    students.remove(students_name)
    print("Student removed successfully")        