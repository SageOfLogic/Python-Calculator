# Simple Calculator in Python
# Author: Rishabh
# Description: Performs basic arithmetic operations.
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    while True:
        choice = input("\nEnter choice (1-5): ")

        if choice == '5':
            print("Thank you for using the calculator!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid choice! Please select between 1-5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue

        if choice == '1':
            print(f"Result: {num1} + {num2} = {add(num1, num2)}")
        elif choice == '2':
            print(f"Result: {num1} - {num2} = {subtract(num1, num2)}")
        elif choice == '3':
            print(f"Result: {num1} × {num2} = {multiply(num1, num2)}")
        elif choice == '4':
            print(f"Result: {num1} ÷ {num2} = {divide(num1, num2)}")

if __name__ == "__main__":
    calculator()
