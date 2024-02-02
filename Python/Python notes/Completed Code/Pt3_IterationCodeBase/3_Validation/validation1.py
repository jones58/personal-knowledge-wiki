"Task 1: In the terminal Enter numeric values for the first and second number to perform addition and take note of the output "
"Task 2: In the terminal Enter a numeric value  for the first number and string value(ten/one/two) for the second number to perform addition"
"and take note of the output"



# num1 = int(input("Enter your first number: "))
# num2 = int(input("Enter your second number: "))
# answer = num1 + num2
# print(f"The answer to {num1} + {num2} = {answer}")
# print("Executing...some code and processes")
# letters = ["A","B","C"]
# for letter in letters:
#     print(letter)


"Task 3: Explain why did the program break, when you followed the instructions in task 2 but not in task 1"



# use try and except to handle exception and errors in your program 
try: # execute he code in the try block
    num1 = int(input("Enter your first number: "))
    num2 = int(input("Enter your second number: "))
    answer = num1 + num2
    print(f"The answer to {num1} + {num2} = {answer}")
   

except ValueError:
    print("You have used the wrong data type!!")

print("Executing...some code and processes")
letters = ["A","B","C"]
for letter in letters:
    print(letter)

# https://www.w3schools.com/python/python_ref_exceptions.asp
# https://docs.python.org/3/library/exceptions.html?highlight=exception#Exception

