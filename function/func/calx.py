import math

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Cannot divide by zero!"
    return x / y

def factorial(x):
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)

def sqrt(x):
    if x < 0:
        return "Cannot find square root of a negative number!"
    return math.sqrt(x)

print("Operations available:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Factorial")
print("6. Square Root")

operation = input("Enter the number corresponding to the operation you want to perform: ")

if operation in ['1', '2', '3', '4']:
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if operation == '1':
        print("Result:", add(num1, num2))
    elif operation == '2':
        print("Result:", subtract(num1, num2))
    elif operation == '3':
        print("Result:", multiply(num1, num2))
    elif operation == '4':
        print("Result:", divide(num1, num2))
        
elif operation == '5':
    num = int(input("Enter a number to find its factorial: "))
    print("Factorial:", factorial(num))

elif operation == '6':
    num = float(input("Enter a number to find its square root: "))
    print("Square Root:", sqrt(num))

else:
    print("Invalid input. Please enter a number between 1 and 6 for the operation.")
