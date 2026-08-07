import day9_calculator

num1 = int(input("Enter first Number: "))
num2 = int(input("Enter second Number: "))


print("1.add")
print("2.sub")
print("3.mul")
print("4.div")

choice = input("Enter your choice: ")
if choice == "1":
    print(day9_calculator.add(num1, num2))
elif choice == "2":
    print(day9_calculator.sub(num1, num2))
elif choice == "3":
    print(day9_calculator.mul(num1, num2))
elif choice == "4":
    print(day9_calculator.div(num1, num2))
    

