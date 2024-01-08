
# X = int(input("Enter first number: "))
# Y = int(input("Enter second number: "))


# A=X
# for i in range(0,Y):
#     A=A-Y
#     print("Your Division is ", A)
    
    
# # print("Your Division is ", Z)
# # print(add(X,Y))
# # print(subtract(X,Y))

# print(X/Y)




X = int(input("Enter first number: "))
Y = int(input("Enter second number: "))

A = X
counter = 0

while A >= Y:
    A = A - Y
    counter += 1

print("Your Division is:", counter)

print(X/Y)