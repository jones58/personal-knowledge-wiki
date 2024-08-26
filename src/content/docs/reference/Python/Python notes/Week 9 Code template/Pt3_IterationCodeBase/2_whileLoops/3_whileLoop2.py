"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""


"To Do: Predict, then Run, and then Investigate"

num = 1  # int(input("Enter a number: "))
userNum = 12
# while 1 <= 20

while num <= 20:  # start from 1 and keep looping to 20(condition is met)
    print(f"The number is {num}")
    if num == userNum:  # check if the value in userNum is the same as the value in num
        print(f"Exited loop")
        break  # break/exit the loop
    num += 1  

"Modify/Make"
"To Do: Task1: modify the userNum variable to use a randomly generated number between 1 - 20"
"Further reading on python while statements"

# https://www.w3schools.com/python/ref_keyword_while.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_reference.asp


