"""Nested selection/nesting is when a selection block(if/else) is placed within another if, 
 else selection block"""


"Predict, then Run, and then Investigate"

userAge = int(input("Enter your age: "))

ageLimit = 16

passCode = "Bootcamp"

# compare if the value held in userAge is greater than the value held in ageLimit
if userAge > ageLimit:
    # execute the code block below if the comparison returns true
    userCode = input("You have met the age requirement\nWhat is the secret code? ").title()
    # nested if will execute if the codition above is true (if userAge > ageLimit:)
    if userCode == passCode:
        print(f"Welcome, your code {userCode} is valid.Access granted ")
     # This else will execute if nested if condition above is false (userCode is not equal to passCode:)
    else:
        print(f"Goodbye, your code {userCode} is invalid. Access Denied!! ")
# This else will execute if the if condition above is false ( userAge is less than the ageLimit:)
else:
    print(f"You are {userAge} years old and below the age limit\nCome back when you are older!! ")


"To Do: Q&A"
"What do you think is the equivalent of JS nested if in python?"


"Modify"
"To Do: Task 1: Using if elif and else"
# Exercise: Modify the code above to use else for both the outer if and the nested if condition



