try:
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    
    print(num1 / num2)
    
except Exception as e:
    print("Error:", e)
else:
    print("Result:", num1 / num2)
finally:
    print("Program Finished.")   