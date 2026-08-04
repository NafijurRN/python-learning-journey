students = {}


for i in range(3):
    name = input("Enter Student Name: ")
    cgpa = float(input("Enter Student CGPA: "))
    students[name] = cgpa
    
print("================Student Records================")
for name, cgpa in students.items():
    print(f"Name:{name}|CGPA:{cgpa}")
        