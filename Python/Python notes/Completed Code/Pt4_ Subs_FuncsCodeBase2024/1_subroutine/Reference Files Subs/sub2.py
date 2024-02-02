
"To Do: Predict, then Run, and then Investigate"
def addition():
    # name is a global variable 
    # answer, num1 and num2 are local variables 
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")

"Make"
"To Do:Task1: Modify the code above to use either subtraction or multiplication or division and change the subroutine name respectively"
def subtraction():
    # ask for user input and store in num1 variable 
    num1 = int(input("Enter your first number: "))
    # ask for user input and store in num2 variable 
    num2 = int(input("Enter your second number: "))
    # subtract the value held in num1 from num2 variable and save it answer variable
    answer = num1 - num2
    # format the answer from the subtraction
    print(f"The answer to {num1} + {num2} = {answer}")


"To Do:Task2: Add comments to the explain your lines of code"


# prevents the automatic running of the subroutine when it is imported
# in to another python file/application
"If this file is run directly it will automatically call and run the respective subroutines"
if __name__ == "__main__":
    addition()

"Further reading on python functions"
# 

