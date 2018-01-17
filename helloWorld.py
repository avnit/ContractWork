import numbers as num
#import numpy as nm
#import panda as py



print("Hello world \n")
def add_number(a,b):
    print( a + b)

add_number(10,18)

#for loop example
for j in range(0,10):
    for i in range(0,10):
        z = i*j
        print("{0} * {1} = {2} \n".format(i,j,z))

#list
student_name = ['avnit', 'Mark' , 'Hansen']
for name in student_name :
    print (name)



#dictionary example

employee = {
    "name" : "avnit",
    "student_id" : 171,
    "feedback" : "awesome employee!!"
}

avnit_feedback = employee["feedback"]
name = employee["name"]
print("{0}'s feed back is {1} \n".format(name, avnit_feedback))

# testing new code here
