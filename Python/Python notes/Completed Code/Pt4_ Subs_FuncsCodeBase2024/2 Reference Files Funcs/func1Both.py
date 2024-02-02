"A subroutine(function) may or may not have a return statement"
"A subroutine(function) may or may not have parameters"

# create function use return statement without parameters and arguments
"To Do: Predict, then Run, and then Investigate"
def user():  # define the subroutine/function user
    name = "Emjay"
    return name

# method 1
print(user())   

def userName():  # define the subroutine userName
    name = input("What is your name? ")
    return name


# method 2
aUser = userName()
print(f"The user is {aUser}")


# create function use return statement with parameters and arguments
def addition(paraNum1, paraNum2, paraAdd):  # defines the addition function
    paraAdd = paraNum1 + paraNum2
    return paraNum1, paraNum2, paraAdd


print(addition(100,200,0))

myAddition = addition(10,20,0)

print(myAddition[0])
print(myAddition[1])
print(myAddition[2])

print(f"The answer to {myAddition[0]} + {myAddition[1]} = {myAddition[2]}")
    # variables inside a  surbroutine/function have local scope
    

# # prevents the automatic running of the subroutine when it is imported
# # in to another python file/application

# # "If this file is run directly it will automatically call and run the respective subroutines"
# if __name__ == "__main__":
#     # call/invoke the subroutine
    
#     # call/invoke the subroutine
  
#     print(f"Method 2\nYour username is {}")

#     # call/invoke the functioneName
#     "Method 1"
    
#     print(f"Method 2\nThe answer is {}")

#     "Method 2"
#     num1 = 10#int(input("Enter your first number: "))
#     num2 = 20#int(input("Enter your second number: "))

#     # Assigned the function to the variable myAddition
   
#     print(f"Method 2\nThe answer is {}")


#     print(f"Your answer to {} + {} is {}")





