"Parameter(s): used in a subroutine/function to allow values to be passed into them/used as a place holder(s)"

"To Do: Predict, then Run, and then Investigate"

# define the subroutine/function addition with parameters par1 and para2
"In the subroutine definition, you pass in the parameter(s)(placeholder(s))"
def addition(para1, para2):
    answer =  para1 + para2
    print(f"The answer to {para1} + {para2} = {answer}")

    "in the subrotuine call, you pass in the argument(s)"
def addNums(paraNum1, paraNum2):
    total = paraNum1 + paraNum2
    print("The answer to", paraNum1, " + ", paraNum2 , " = ", total)



# firstPara = 1
# secondPara = 2

"Make/Modify"
"To Do: Task 1 : Modify the subroutine call below to pass in you own name as an argument "
def user(paraFName,paraLName):
    # name = input("Enter a name: ")/
    print("Your name is", paraFName + " " + paraLName)
user()

# from sub1 import *

if __name__ == "__main__":
    addNums(1,2)
    addNums(11,2)
    addNums(12,2)
    addNums(13,2)
    user("Keanu", "Reeves")
    user("Abdul", "Malik")
    user("James", "Bond")
    


    # Method 1
    # in the subroutine call we pass in the integer values(1,2) within the braces as an argument to be passed
    # into the parameters par1 and para2
  
   
    # Method 2
    # in the subrotuine call we pass in the variable name  within the braces as an argument to be passed
    # into the parameter paraUname
    #in the subroutine call we pass in the num1 and num2  within the braces as an argument to be passed
    #into the parameters par1 and para2
  
   

