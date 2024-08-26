"Read through the print statement formating examples and reference or use it as a guide during lesson"
"To DO: For further reading and independent learning refer to the link below"
# https://www.w3docs.com/learn-python/python-comments.html
"Objectives"
"" '' # Formating print statements
"" '' # Formatting strings:



print("Hello\n" *3)
print("All the power\n is within you")
num1,num2=10,5
print(num1,num2) # without seperator
""" Use of seperator function """
print(num1,num2, sep=',')# the separator seperates the data printed using the separator character used

"""create and assign values to variables"""
name = "Peter"
score =  96.8995

"""formatting print statement"""
print("Name is", name, "Score is", score)

"""Use of place holders(i% s% f% and special formatting strings to format print statement"""
print("Name is %s, Score is %f"% (name,score)) # %

"""Use of place holders(i% s% f% and special formatting strings to format print statement"""
print("Name is %s, Score is %.2f"%(name,score)) # use the .2f to round to two decimal places

"""Use of curly braces  places holders and string format function to format print statement"""
print("The student Name is {},and his score is {}".format(name ,score)) #Use of curly braces places holders,

"""Use of curly braces places holders, indexes and string format function to format print statement"""
print("The student Name is {0},and his score is  {1}".format(name ,score)) #Use of curly braces places holders, indexes


#  Why use f-strings
print(f"The value for score using f-string is  {score}")
print(f"The student Name is {name} ,and his score is {score}")
print("The value for score is " + str(score))
print("The value for name is ", name)


"To DO: For further reading and independent learning refer to the links below"
# https://docs.python.org/3.11/library/stdtypes.html?highlight=str#printf-style-string-formatting
# https://realpython.com/python-f-strings/
