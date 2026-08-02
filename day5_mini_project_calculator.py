def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b != 0:
        return a/b
    else:
        return "Error: Division by zero is not allowed."

print("===========Simple Calculator===========")
    
print("\nSelect Operation: ")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide") 
print("5. Quit") 

def main():
    while True:
        choice = input("\nEnter choice (1/2/3/4/5): ")
        if choice == '1':
            print(add(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
        elif choice == '2':
            print(subtract(float(input("Enter first Number: ")), float(input("Enter Second Number: "))))
        elif choice == '3':
            print(multiply(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
        elif choice == '4':
            print(divide(float(input("Enter First Number: ")), float(input("Enter Second Number: "))))
        elif choice == '5':
            print("Exiting the calculator.")
            break
        else:
            print("Invalid input. Please enter a valid choice.")

main()