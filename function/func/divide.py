# # Division Function 

X = int(input("Enter first number: "))
Y = int(input("Enter second number: "))
def divide(X, Y):
    A = X
    counter = 0
    while A >= Y:
        A = A - Y
        counter += 1
    return counter

quotient = divide(X, Y)
remainder = X % Y
# print(remainder)
# # print("Result:", "{:.1f}".format(quotient))

if(remainder >  0):
    remainder=remainder*100
    quotient2=divide(remainder,Y)
    remainder1 = remainder % Y
    # print(quotient2)
    # print(remainder1)
 
# Convert quotient to an integer and then to a string
quotient = int(quotient)
quotient = str(quotient)

# Convert quotient2 to a string
quotient2 = str(quotient2)

# Concatenate both parts
result = quotient  + "." + quotient2

print("Result:", result)

  
    
# print("Result:", "{:.1f}".format(quotient)+ (int(quotient2)))
# print(quotient)
# print(remainder)




# def custom_divide(X, Y, precision):
#     integer_part = X // Y
#     result = str(integer_part) + "."

#     remainder = X - integer_part * Y
#     while precision > 0:
#         X = remainder * 10
#         quotient = X // Y
#         result += str(quotient)
#         remainder = X - quotient * Y
#         precision -= 1

#     return result

# X = float(input("Enter first number: "))
# Y = float(input("Enter second number: "))
# precision = int(input("Enter the precision for decimal places: "))

# result = custom_divide(X, Y, precision)
# print("Result:", result)


