
"As your programs become larger and more complex, they need to be broken down into smaller, self-contained sections"
"In python function is a type of subroutine, asubroutine is sequence of instructions to perform a specific task with an identifiable name."

"A subroutine(function) definition is used to define the steps within the subroutine(function)"

"A subroutine(function) may or may not have a return statement"

"A subroutine(function) may or may not have parameters"

"def just defines the subroutine(function)"

"A subroutine(function) is not executed unless the subroutine is called."

"A subroutine(function) call tells the program to branch to the function, execute it and come back to the next statement in the main program"

"Custom built function"  '' # A function that you have created yourself and imported into other programs that you have created.

# Syntax
"""
def subroutine/functionName():
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)
    subroutine/functionBody(code)

#call/invoke the subroutine/function
subroutineName/function()


"""

"To Do: Predict, then Run, and then Investigate"
# name is a global variable 
# name = "Emjay"
# print("Your name is: ", name)

# name = input(("What is your name? "))
# print("Your name is: ", name)


# def define the subroutine/function user
def user():
    name = "Emjay"
    print("Your name is", name)

# user()

# Global scope variable /#
name = "Abdul"

def userName():
    # name is a now a local variable 
    name = input(("What is your name?: "))
    print("Your have entered", name)

# def define the subroutine userName
# userName()


# print("The gloabal name", name)
# print("Welcome")
# userName()

"To Do: Task 1: Call the subroutine inside a print function with or without f-strings and explain your result"
# print(f"{user()}")



"Modify/Make"
"To Do: Task 2: Modify the subroutine to ask for address and interest"
def userdata():
    address = input("Enter your address: ")
    interest = input("Enter your interest: ") 
    print(f"Your {address} and {interest}")
    


'Task 2: Investigate  if __name__ == "__main__":'
'Copy and paste the code block above if __name__ == "__main__":  in the browser to investigate it use'

# from subPara1 import *


if __name__ == "__main__":
    # Add comment to explain why it can be used in your program in your own words"
    user()
    userName()
    # addNums(2,1000)
    userdata()
# call/invoke the subroutine
# call/invoke the subroutine
  
    "Knowledge Check"
    "Task 4: Linking existing knowledge with new knowledge"
# What do you think is the equivalent of the python 'def' keyword in JavaScript

"Further reading on python functions"
# 


