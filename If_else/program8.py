# check Quadrant


X = int (input("Enter a Quadrant: "))
Y = int(input("Enter a Quadrant: "))

if( X==0 and Y!=0 ):
    print(" Lies on the Y-aXis.")
elif(X!=0 and Y==0):
    print("Lies in X-aXiX.")
elif X > 0 and Y > 0:
    print("Lies in the 1st quadrant.")
elif X < 0 and Y > 0:
    print("Lies in the second quadrant.")
elif X < 0 and Y < 0:
    print("Lies is in the third quadrant.")
elif X > 0 and Y < 0:
    print("Lies is in the fourth quadrant.")
else:
    print('Origin')
        