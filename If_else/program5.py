# three  number comparsion which one is the largest


numb1 = int(input("Enter number 1: "))
numb2 = int(input("Enter number 2: "))
numb3 = int(input("Enter number 2: "))

if(numb1 > numb2 and numb1> numb3):
    print("Number1 is the greatest")
elif(numb2 > numb1 and numb2> numb3):
    print("Number2 is the greatest")
else:
    print("number 3 is the greatest")