"""
Break in Python Python break is generally used to terminate a loop. 
This means whenever the interpreter encounters the break keyword, 
it simply exits out of the loop. Once it breaks out of the loop, 
the control shifts to the immediate next statement.
"""


"To Do: Predict, then Run, and then Investigate"

#Combining iteration and Selection"

numList = [1, 3, 4, 6, 1, 3, 5, 7]

found = False
for number in numList:
    if number == 30:
        print("Found", number)
        found = True
        break
    else:
        print(f"Number {number} not found")

if not found:
    print("Number 3 not found in the list")

#  uses a boolean variable found to keep track of whether the number 
# 3 has been found in the list. If the number 3 is found, the found 
# variable is set to True and the loop is exited with the break statement.
#  If the loop completes without finding the number 3, the code checks 
#  the value of found and prints a message indicating that the number was not found.

"Modify/Make"
"To Do: Task 1: You have been provided with a list of modules below, write a for loop similar to the one above to break out of the loop when 'Python' is found"
#Refer to the code above to gide you in completing this task

