#this is my first python program and it's an example of one line comment

print("hello world")
print ("My name is Nafijur Rahman")
print ("I am a CSE student")
print ("I am Learning Python Programming Language")

#variable declaration and initialization  
name = "Nafijur Rahman"
age = 23
cgpa = 3.69

print ("My name is", name)
print ("My age is ",age)
print ("My CGPA is ",cgpa)

#Multiple variable printing 
print("My name is",name, "and my age is",age,"and my CGPA is",cgpa)

#Basic data types (string, integer, float, boolean)

#String data type for storing text 
name = "Nafijur Rahman Nasrat"

#Integer data type for storing whole numbers 
age = 23

#Float data type for storing decimal numbers 
cgpa = 3.69

#boolean data type for storing true or false values 
is_student = True

#cheaking the data types in python using type() function 

print ("Data type of name is", type(name))
print ("Data type of age is", type(age))
print ("Data type of cgpa is", type(cgpa))
print ("Data type of is_student is", type (is_student))



#how to take input from user in python using input() function
name = input("Enter your name: ")
print("Hello", name)

age = int(input("Enter your age: "))
print("You are",age,"years old")