# Selection is used to control the flow of the program

score = int(input("Enter a number: ")) # score variable global scope
"Predict, then Run, and then Investigate"

# check the condition that score is greater than 100
if score > 100 or score < 0:
    # create avariable and assign it the value Invalid Entry
    grade = "Invalid Entry"

# check the condition that score is between 75 and 100
elif score >= 75 and score <=100:
    grade = "A" # re-assign the value of the grade variable
    # create avariable and assign it the value A

# check the condition that score is between 60 and 74
elif score >=60 and score <=74:
    # reassign the grade variable the value B
    grade = "B"

# check the condition that score is between 50 and 59
elif score >=50 and score <=59:
    # reassign the grade variable the value C
    grade = "C"

# reassign the grade variable the value F
else:
    grade = "Ungraded"
print(f"You have scored {score} and your grade is {grade}")

"To Do: Q&A"
"What do you think is the equivalent of JS else if in python?"


"Make"
"To Do: Task 1: Using if elif and else"
# Create a Menu program that allow user to select between three subject choices
# User must be presented with the value assoiciated with each choice
# for example 1. Music, 2. Maths ....
# A choice must also be available for the user to exit the program
# A message using the print function must be display as per the user choice

"To Do: Task 2:"
# Use if else to find item(a specific number) from a list
numList = [56, 78, 100, 45, 88, 71]
