
# Babylonian Method (Heron's Method):
# number=1/2*(guess+x/guess)



""""
400 20
200 doesn't have a perfect square
1-400
1-400

loop
11 22 33 44 = 400>400


"""
num2 = int(input("Enter first number: "))
num1 = int(input("Enter second number: "))
def mul(num1,num2):
    mul=0
    for i in range(num2):
        mul+=num1
        return mul
def sqrt(num):
    for i in range(num):
        if mul(i,i)==num:
            return i
        elif mul(i,i) > num:
            return "Not perfect square"

    
print(sqrt())
    
    