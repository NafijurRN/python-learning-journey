try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    result = num1 / num2
except Exception as e:
    print("Error:", e)
    
else:
    print("Result:", result)
    
finally:
    print("Program Ended.")
    


