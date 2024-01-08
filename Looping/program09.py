

#        *
#      *   *
#    *       *
#  ************ 

#Triangel

length =4
e=0
# print(" "*(length) + "*"  )
for i in range(length-1,0,-1):
    print(" "*(i) + "*" + " "*e +"*" )
    e+=2
print("* "*(length)   )

# 4  2 
# 3    4
# 2    6
# 1    8
#       *
#     *  *
#    *    *
#   *      *
