
"Further reading on datatypes in python"
# https://docs.python.org/3/library/stdtypes.html#tuple
# https://docs.python.org/3/library/stdtypes.html#set
# https://www.w3docs.com/learn-python/python-data-types.html

"Objecttives"
"" '' # Data types
"" '' # set 


"A set is an unordered list"


"Predict, then Run, and then Investigate"
set1 = {10,20,30, "xyz", "abc"} # once a set is created the values/items can not be changed 
print(type(set1))
print(set1)

set1.update([1,4,"bcd"]) # set can be updated with new items/value
print(set1)

set2={4,7, "paul", "peter"}
set1.update(set2)
print(set1)

set1.remove("peter")# items in a set can ony be removed using the name/value of the set item not via index 
print(set1)


"To Do: Investigate and exlain in your own words the purpose of the forLoop in the code block below"
# Add an element to a set.
set1.add("Python") # new items/value can be added to a set after creation
print(set1)
for i in set2:
    print(i)

set3 = {21,22,23,"John"}
print(set3)

set4 = input("Enter Value: ")
print(set4)


"Modify:"
"To DO:"
# Modify the data structures above by changing their values or oject names


"Make:"
"Task 1: Follow the set examples above to create a set with five countries"
# print the items(countries) in the set 
# add two more countries
# delete a counry of your choice
# print the set items


"Predict, Run and Investigate the frozen set"
fSet3 = frozenset(set3)
print(fSet3)


"Make:"
"To DO: Try to add an item to frozen set 'fset' and explain the outcome"

