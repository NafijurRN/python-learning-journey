#general style 
file = open ("student.txt", "w")
num1=input("Enter Student Name: ")
num2=input("Enter Student Name: ")
num3=input("Enter Student Name: ")
file.write(f"Student 1: {num1}\nStudent 2: {num2}\nStudent 3: {num3}")
file.close()




#industry style code 
with open("student.txt", "w") as file:
    for i in range(3):
        name = input("Enter Student Name: ")
        file.write(name + "\n")
        