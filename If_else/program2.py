# checking leap year
#2000 is leap year and 2001 is not
# to check this

numb = int(input("Enter a number: "))
if(numb%4==0):
    print("this is a leap year")
else:
    print("this is not a leap year")