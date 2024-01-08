# dictionary


"""
a=[1,2,3,4] C struct
b=a b is the refreneces to a

"""
#LIST
# a=[1,2,3,4]
# b=a

# b[1]=5

# print(a)
# print(b)
#copy

# a="aqsa"
# b[0]="A"
# print(b)


#dICTIONARY
#key value pair  {Key:Value, key:value}
# student={
#     'name':"aqsa",
#     'batch':'15sw',
#     'dept':'computers'
# }

# print(student['name'])
# print(student['batch'])

#list

name =["Alan","Joha"]
batch=["19","18"]
dept=["maths","physics"]

student={
    'name':"aqsa",
    'batch':'15sw',
    'dept':'computers',
    'dept_choice':['sw','ee'],
     'address':{
         'stree':'kk',
         'house':'ddd'
     }
}

print(student['address']['house'])
# },
# {
#     'name':"owais",
#     'batch':'15sw',
#     'dept':'computers'
# },{
#     'name':"zoha",
#     'batch':'15sw',
#     'dept':'computers'
# }

# student['id']='12hjh'
# student['dept']='sw'
print(student.pop('dept'))
del student['dept']
#  print(student)



