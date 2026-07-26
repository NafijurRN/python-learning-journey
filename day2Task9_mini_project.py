Student_Name = input("Enter your name:")
Student_ID = input("Enter your ID: ")

Bangla_marks = int(input("Enter your Bangla marks: "))
English_marks = int(input("Enter your English marks: "))
Math_marks = int(input("Enter your Math marks: "))



print("------------Student Result------------")

if Student_Name == "Nafijur" and Student_ID == "1234":
    print("Login Successful")
else:
    print("login Failed")
    
    
Total_marks = Bangla_marks + English_marks + Math_marks
print("Total marks:", Total_marks)

Average_marks = Total_marks /3
print("Average marks:", Average_marks)

Grade = ""

if Average_marks >=80 and Average_marks <=100:
    Grade = "A+"
elif Average_marks >=70 and Average_marks <=79:
    Grade = "A"
elif Average_marks >=60 and Average_marks <=69:
    Grade = "B"
elif Average_marks >=50 and Average_marks <=59:
    Grade = "C"
elif Average_marks >=40 and Average_marks <=49:
    Grade = "D" 
    
elif Average_marks >=0 and Average_marks <=39:
    Grade = "F"
    
print("Grade:", Grade)
    
Status = ""
if Average_marks >=40 and Average_marks <=100:
    Status = "Pass"
elif Average_marks >=0 and Average_marks <=39:
    Status = "Fail"   
    
print("Status:", Status) 


    
    