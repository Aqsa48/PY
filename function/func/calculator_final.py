import math
# Addition Function
def add(x,y):
    result= x+y
    return result
# Subtraction Function
def subtract(x,y):
    result= x-y
    return result
# Multiplication Function
def multiply(X, Y):
    Z = 0
    for i in range(0, Y):
        Z = X + Z
    return Z

# Division Function 
def divide(X, Y):
    A = X
    counter = 0
    while A >= Y:
        A = A - Y
        counter += 1
    return counter

def divide_decimal(X, Y):
    quotient = divide(X, Y)
    remainder = X % Y

    if remainder > 0:
        remainder = remainder * 100
        quotient2 = divide(remainder, Y)
        remainder1 = remainder % Y
        quotient = int(quotient)
        quotient = str(quotient)
        quotient2 = str(quotient2)
        result = quotient  + "." + quotient2
        # print(result)
        return result
    else:
        return quotient
    
    
    
# By using the functions 
def factorial(X):
    for i in range(1, X):
        X = multiply(X,i)
    return X


def sqrt(X):
    if X < 0:
        return "Cannot find square root of a negative number!"
    return math.sqrt(X)


print("Enter 1,2,3,4,5 or 6 for numbers to perform")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Factorial")
print("6. Square Root")

number = input("Enter the number")

if number in ['1', '2', '3', '4']:
    X = int(input("Enter first number: "))
    Y = int(input("Enter second number: "))
    if number == '1':
            print("Result:", add(X, Y))
    elif number == '2':
        print("Result:", subtract(X, Y))
    elif number == '3':
        print("Result:", multiply(X, Y))
    elif number == '4':
        # print("Result:", divide(X, Y))
        divide(X, Y)
        print("Result=", divide_decimal(X, Y))
        
elif number == '5':
    num = int(input("Enter a number to find its factorial: "))
    print("Factorial:", factorial(num))

elif number == '6':
    num =int(input("Enter a number to find its square root: "))
    print("Square Root:", sqrt(num))

else:
    print("Invalid input. Please enter a number between 1 and 6 for the number.")