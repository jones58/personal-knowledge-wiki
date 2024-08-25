# The default data type for the input function is string
# The input function allow the program to take user input
"Objectives"
"" '' # Casting and/or conversion

userAge = int(input(("Please enter your age: ")))
print(type(userAge))
print("Your age is: ", userAge)

"To DO: Exercise: Provide screenshot to the anwers to the questions below in the chat"

# To DO:
# what is the equivalent of input in JavaScript?

prompt("Please enter your age: ")

# what is the equivalent of converting a string to integer inJavaScript?

num = parseInt("123")


# Format the print statment using f-string

print(f"Your age is: {userAge}")

"To DO: Task 2: Working with the input function and datatypes"

num1 = input("Enter your first number: ")
# To complete the code block above
# Use a variable and invoke the input function ask for a second number
# Add the two numbers
# print out the total of the two numbers
# Format your print statement to read, The answer to num1Value + num2Value is TotalValue
num2 = input("Enter your second number: ")
num1Value = int(num1)
num2Value = int(num2)
TotalValue = num1Value + num2Value
print(f"The answer to {num1Value} + {num2Value} is {TotalValue}")



"To DO: Task 3: Working with the input function and datatypes"
# Modify you solution above to take in decimal values instead of whole numbers

num1Value= float(input("Enter your first number: "))
num2Value= float(input("Enter your second number: "))
TotalValue = num1Value + num2Value
print(f"The answer to {num1Value} + {num2Value} is {TotalValue}")
