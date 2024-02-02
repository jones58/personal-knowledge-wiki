"""Nested selection/nesting is when a selection block(if/else) is placed within another if, 
 else selection block"""


"""Nested selection/nesting is when a selection block(if/else) is placed within another if, 
 else selection block"""



"To Do: Predict, then Run, and then Investigate and then comment the code to explain each line of code does"

pyCourse = float(input("Enter your Python score: "))
htmlCourse = float(input("Enter your HTML score: "))
sqlCourse = float(input("Enter your SQL score: "))

if pyCourse < 45:
    print(f"Try again in python {pyCourse}")
elif htmlCourse < 45:
    print(f"Try again in HTML {htmlCourse}")
elif sqlCourse < 45:
    print(f"Try again in SQL {sqlCourse}")


else:
    gradesAverage = (pyCourse + htmlCourse + sqlCourse)/ 3
    if gradesAverage <= 55:
         print(f" Your average score is {gradesAverage} and is Grade C ")
    if gradesAverage <= 79:
         print(f" Your average score is {gradesAverage} and is Grade B")
    if gradesAverage <= 89:
         print(f" Your average score is {gradesAverage} and is Grade B ")





