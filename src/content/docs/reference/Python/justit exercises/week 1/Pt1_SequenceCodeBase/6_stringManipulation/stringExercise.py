"Further reading on string  in python"
# https://www.w3docs.com/learn-python/python-strings.html

"Predict, then Run, and then Investigate"
s1 = "I am a python programmer"  # string
s2 = "I am a python programmer with single quote"  # string
s3 = """I am a python programmer with single quote I am a python programmer with 
single quote I am a python programmer with single quote"""
s4 = "How are you "

# print character 5 from the string held in the variable s1 as per index position/value
print(s1[5])


"Make"
"To Do: Task 1a: print characters in index posion 7,8,10,12,50, share your solution as screenshot in the chat " 

"To Do: Task 1b: If you get an index error please investigate(research) and explain in your own words, share explnation as screenshot in the chat"


# Returns the length of the string
print(len(s1))

# Slice the string
"Predict, then Run, and then Investigate"
"Use the link below to investigate python string ans string slicing"
# https://www.w3docs.com/learn-python/python-strings.html

print(s1[5:12])  # start and end index postion
print(s1[5:])  # specify start index position and every character that follows
# use - with value to specify character from the end that should be omitted
print(s1[5:-1])  
print(s1[5:-2])

"Make"
"To Do: Task 2a: print up to the 12 item as per index position using the slicing method, share your solution as screenshot in the chat  "


"Predict, then Run, and then Investigate"
s5 = "This is it, I am a python programmer"  # string
print("\n")
print(s5)
print(s5[-29:15])  # we write this
print(s5[:15])  # python see this
print(s5[1::3])  # without specifying the end index position


# print specific characters within the start and end index position specified
print(s5[1:22:2])  # start index , end index and print every second character



# String methods used to perform operations on strings
" Use the link below to investigate python string methods"
# https://www.w3docs.com/learn-python/python-strings.html
# use find method to find /locate a subsring within a given string

"Task 2b: perform operations on strings"

"Modify"
"To Do: Complete the code below find method to find /locate subsring substring 'are' within a given s4 variable "
print(s4.?("?"))

s5 = " It is a beautiful day A wonder "
"Modify"
"To Do: Complete the code below using the strip(), rstrip(), lstrip() methods to strip string of white spaces
s4.rstrip()
print(s5)
print(s5.?())  # strip before the sentence
print(s5.?())  # strips after the sentence
print(s5.?())  # strips before and after the sentence

"Modify"
"To Do: Complete the code below using the count() method to count the number of times the letter 'a' appear in the string held in s5"
# count the a specific character
print(s5.?("?"))


"Complete the code below using the  upper, and lowe methods to change the character to upper and lower case in the string held in s5"
print("This is lower case: ", s5.?())
print("This is Upper case: ", s5.?())

"Modify"
"To Do: Complete the code below using the title method to change the first character to title case in the string held in s5"
print("This is Title case: ", s5.?())

"Modify"
"To Do: Complete the code below using the replace method to replace the substring 'day' with the word 'weather' in the string held in s5"
# replace substring within a string
print(s5.?("day", "?"))  # use replace function to replace a subsstring

