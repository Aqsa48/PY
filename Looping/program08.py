# Hollow Diamon    
#    *
#   *  *
#  *    *
# *      *
#  *    *
#    * *
# #     *
# length=5;
# print(" "*(length-1)+"*")

# for i in range(2,length+1,2):
#     print(" "*(length-i) + "*" + " "*i +"*" )

#Diamond

length = 3
even = 2
print(" "* (length-1)+"*")
for i in range(length-2,0,-1):
    print(" "*(i) + "*" + " "*even +"*" )
    # print(i,even)
    even+=2
for i in range(1,length-1,):
    even-=2
    # print(i,even)
    print(" "*(i) + "*" + " "*even +"*" )
print(" "* (length-1)+"*")



# print(" "*4+"*")
# print(" "*3+"*"+" "*2+"*")
# print(" "*2+"*"+" "*4+"*")
# print(" "*1+"*"+" "*6+"*")
# print(" "*2+"*"+" "*4+"*")
# print(" "*3+"*"+" "*2+"*")
# print(" "*4+"*")



# length=5;
# print(" "* (length+1) + "*")
# for i in range(0,length):
#     # print(" "*(length-1) + "*"*i + " " *(length-1))
#     # print( " "*(length-i) +"*"  + " " *(length) +"*")
#     print( " "*(length-i) +"*" + " "*(i+2) +"*")
# for j in range(0,length):
#     print( " "*j +"*" + " "*(length+2-i) + "*")