"List methods"
"""You can think of list methods as special functions that are applied to lists. 
To call a list method, you need to use dot notation (as in the examples that follow).  """
"Method" '' # A function that belongs to an object.
    #  Use list methods to:"
    #  list.append(item)"        # add item at end of list
    #  list.insert(index,item)   "  # add item at index
    #  list.pop(index)"       # remove item at index
    #  list.remove(item)   "  # remove item
    #  list.index(item)   "  # search for index of item
    #  list.count(item)"  # get occurrences of item
    #  list.reverse()"   # reverse list
    #  list.sort()"      # sort list


"Method"  # A function that belongs to an object.
"Custom  built function"  # A function that you have created yourself and imported into other programs that you have created.
"List"  # A dynamic data structure that holds items under one name. The items can be of varying data types.


"Traverse" ''  # Move through a sequence.
"You can use a for loop to traverse a list of elements"
#              0         1         2        3          4      5       6
trainers =  ["Abdul", "Christian","Narayan","Richie","Tim", "Waqas", "Zak"]
for trainer in trainers:
    if trainer == "Tim":
        print("Python")
    else:
        print("HTML")
"To Do: Task 1: Predict, run and investigate the code above"

"To Do: Task 2: "
"" '' # Your task is to traverse through the variable 'course' provided below using a for loop and you are not required to search for a specific element
course = "Python Programming"


"Objective "
"" '' # List methods: Recap

"To Do: Task 3: "
"Use any two list method from above to perform operation on the list, listOfNames"


"To Do: Task 4: Predict, run and investigate the code above"
#                  0         1         2        3         4        6       7
listOfNames = ["Nicole", "Laura", "Silvia", "Steve", "Juliet", "Laura", "Silvia"]
print(listOfNames)  # Prints the list
print(listOfNames[2])  # Prints Silvia

"What is the len() used for in the code below?"
for index in range(len(listOfNames)):
    print(f"{index} : {listOfNames[index]}")

print(f"\n{listOfNames}")
# What item is returned from the list and why?
print(f"{listOfNames[3]}\n")


# Note 
"" '' # Refer to https://www.w3docs.com/learn-python/python-lists.html if you find on any of the tasks  
