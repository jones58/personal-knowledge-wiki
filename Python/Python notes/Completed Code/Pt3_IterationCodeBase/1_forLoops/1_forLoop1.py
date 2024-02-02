"Iteration is the repetition of code blocks. For example, a while loop or a for loop."
# for loops is used when you have definite iteration (the number of iterations is known).
# for loop also controls the flow of execution in a program
# For loop is used for iterating through sequences. 


"for loop Syntax"
# for this sequence:
#     do this

"For loops can be used for many types of sequence, for example"
# Letters in a word
# Items in a list
# Numbers in a range
 

"To Do: Predict, then Run, and then Investigate"
"To Do: Explain the difference bewtween the Character in name code block and the name code block?"

print("Character in name  code block ")
letterInName = "Tim Jones"
print(f"The first character is: {letterInName[0]}")
print(f"The second character is: {letterInName[1]}")
print(f"The third character is: {letterInName[2]}")
print(f"The fourth character is: {letterInName[3]}")
print(f"The fifth character is: {letterInName[4]}")
print(f"The sixth character is: {letterInName[5]}")
print(f"The seventh character is: {letterInName[6]}")
print(f"The eighth character is: {letterInName[7]}")
print(f"The tenth character is: {letterInName[8]}")


"Loop through letters in a word"
print("\nname code block")
name = "Tim Jones"
# for something in this sequence:
for aCharacter in name:
#     do this
    print(aCharacter)


"Loop through items in a list in a word"
print("\n")
names = ["Tim", "Zak", "Waqas", "Abdul", "Chris", "Richie", "Narayan"]

for aName in names:
    print(aName)


"Loop through numbers in a range"
"syntax" # for variableName in rangeObject(numberOfIteration)

"for loops that use the range() function"
# range() is the sequence that you are going to iterate through
# range() is a built-in function just like input(). 

"start defaults to 0, and stop is omitted! range(4) produces 0, 1, 2, 3"
for nums in range(4):
    print(nums)
# range(start, stop[, step]) 
'range(start, stop, step) '

# Modify the above to include the start value, stop vale and step value 

"Make"
"To Do: Task 1: Create a program that uses a for loop to iterate through the letters in your name"
username = "Zein Sharif"
for char in username:
    print(char)

"Further reading on python for statements"
# https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements
# https://www.w3schools.com/python/ref_keyword_for.asp