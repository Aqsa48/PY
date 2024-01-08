



X = int(input("Enter first number: "))
Y = int(input("Enter second number: "))

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

print("\n")
print("Your Addition is ", add(X,Y))
print("Your Subtraction is:", subtract(X,Y))
print("Your Multiplication is ", multiply(X,Y))
print("Your Division is:", divide(X,Y))