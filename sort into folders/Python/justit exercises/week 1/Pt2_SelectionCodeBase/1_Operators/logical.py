"Read through the Logical operators examples and reference or use it as a guide during lesson"
"To DO: For further reading and independent learning refer to the link below"
#https://www.w3schools.com/python/gloss_python_comparison_operators.asp

"Logical expression evaluates to True or False"
# Logical operators: and , or, not

# ==    equal  ( 2 == 2)
# < 	less than
# > 	more than
# <= 	less than or equal to
# >= 	greater than or equal to
# !=    Not equal to

num1 = 10  # static object/value
num2 = 5  # static object/value
num3 = 11  # static object/value
num4 = 2  # static object/value
# comparison operator
print(num1 == num2)
print(num1 == 10)
print(num2 == 5)


"Task 1: Predict, then Run, then Investigate, and then add comments"

# Logical operator: and
print("Logical operator: and")

print(num1 == 10 and num2 == 5)
print(num1 == 10 and num2 == 50)
print(num1 == 15 and num2 == 5)

# Logical operator: or
print("Logical operator: or")
print(num1 == 10 or num2 == 5)
print(num1 == 10 or num2 == 50)
print(num1 == 15 or num2 == 5)


# Logical operator:not
print("Logical operator: not")
print(not (num1 == 10))

# Logical operator:not
print("Logical operator: not with or")
print(not (num1 == 10 or num2 == 5))
print(not (num1 == 10 or num2 == 50))
print(not (num1 == 15 or num2 == 5))


# Logical operator:not
print("Logical operator: not with and")
print(not (num1 == 10 and num2 == 5))
print(not (num1 == 10 and num2 == 50))
print(not (num1 == 15 and num2 == 5))