try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = num1 / num2
    
except Exception as e:
    print("Error:",e)   #error message will be printed if any error occurs
    
else:
    print("Result:", result) #error will not be printed if no error occurs and result will be printed
           