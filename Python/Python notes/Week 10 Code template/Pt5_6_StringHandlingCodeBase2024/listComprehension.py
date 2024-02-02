" List comprehension is a concise way to create lists"
"""list comprehension gives us easy to use syntax to 
create one list out of another while applying some logic 
and condition. List syntax comprehension goes into square brackets
"""


"Objective"
"" '' # Use List comprehension to create one list out of another list
"" '' # Compare list comprehension with non list comprehension syntax 
"" ''# Note: List comprehension consists of square brackets containing an expression followed by a for clause

# index    0  1   2  3  4  5 .............
# aList = [1, 2,  3, 4 ,5]
# bList = [6, 7, 8,  9, 10

"To Do: Predict, then Run, and then Investigate"
aList = [1, 2, 3, 4, 5]
bList = [6, 7, 8, 9, 10]

print(aList)
print(bList)

print(aList[2])
print(bList[3], bList[4])

# joined lists
joinedList = aList + bList
print(f"The joined list\n{joinedList}")


# Slicing items  from two lists

slicedItems = aList[0:3] + bList[1:4]
print(f"Sliced List\n{slicedItems}")

"Objective"
"" '' # Use List comprehension to create one list out of another list
# add values from one list to another
"List comprehension"
listAB = [aList[i] + bList[i] for i in range(len(bList))]
print(f"The addedd items from listA {aList} and listB{bList}\n{listAB} ")


# Find common list items
cList = [1, 2, 3, 4, 5, 12, 13, 14, 15, 20, 21]
dList = [6, 7, 8, 9, 10, 4, 5, 12, 13, 14, 30]
print(f"{cList}\n{dList}")

"Objective"
"" '' # Compare list comprehension with non list comprehension syntax 

"This is not list comprehension"

        print(f"The common numbers in c and d lists:{nums}")


"Objective"
"" '' # Use List comprehension to create one list out of another list
"This is List comprehension"

print(f"The common numbers in both list c and d using list comprehension:\n{commonNums}\n")


"Objective"
"" '' # Compare list comprehension with non list comprehension syntax 
"This is not list comprehension"
squareNums = []



"Objective"
"" '' # Use List comprehension to create one list out of another list
"List comprehension"

print(f"List comprehension\n{squareNums}")


"To Do: Extension Tasks: "
# Task 1: sort and print the items in the commonNums variable in ascending and descending order

# Task 2:  create two lists with at least two/three common names in both lists
# find the common names from both lists and put them in a commonNames List
# use the input and then the if to search the common names list for a specific name
# Task 3 : Slice list aList from 0 - 5 and bList from 0 - 4 and put them together in a new list

"Further reading on List Comprehension"
# https://docs.python.org/3/tutorial/datastructures.html
# https://docs.python.org/3/tutorial/datastructures.html#using-lists-as-stacks
# https://docs.python.org/3/library/functions.html#zip