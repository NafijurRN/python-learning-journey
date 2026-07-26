#Nested_if 

username =input("Enter your username: ")
password =input("Enter your password: ")

if username=="Nafijur":
    if password=="1234":
        print("Login Successful")
    else:
        print("Incorrect Password")
else:
    print("Username not found")