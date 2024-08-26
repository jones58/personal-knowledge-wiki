"Read through the assignment operations examples and reference or use it as a guide during lesson"
"To DO: For further reading and independent learning refer to the link below"
#https://www.w3schools.com/python/gloss_python_assignment_operators.asp


""" assigned same value to multiple variables"""
num1=num2=num3=10
print(num1,num2,num3)

"""use of  compound assignment a+=b """
num4,num5=10,5
#print(num4 -5," + ",num5 , "=", num4)
num4+=num5# #compound assignment
print("Addition",num4)

num4,num5=10,5
num4-=num5# #compound assignment
print("Subtraction",num4)

num4,num5=10,5
num4*=num5# #compound assignment
print("Multiplication",num4)

num4,num5=10,5
num4/=num5# #compound assignment
print("Division",num4)

num4,num5=10,5
num4%=num5# #compound assignment
print("Modulus",num4)

num4,num5=10,5
num4**=num5# #compound assignment
print("Power",num4)

num4,num5=10,5
num4//=num5# #compound assignment
print("Floor Division",num4)