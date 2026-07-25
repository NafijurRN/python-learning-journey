number1 = int(input("Enter the first number: "))
number2 = int (input("Enter the second number: "))

print("Select any operation from the following list:")
print("1. Sum")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
operation = int(input("Enter your choice: "))

if operation == 1:
    result = number1 + number2
    print("Result:", result)
elif operation == 2:
    result = number1 - number2
    print("Result:", result)
elif operation == 3:
    result = number1 * number2
    print("Result:", result)
elif operation == 4:
    result = number1 / number2
    print("Result:", result)
else:
    print("Invalid choice!")
