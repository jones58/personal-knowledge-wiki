"""use a while loop when the number of iteration is unknown(dont know how many times you want/going 
to do something for)
A while loop also controls the flow of execution in a program"""



# import the datetime library/class/module
import datetime


"To Do: Predict, then Run, and then Investigate"



print("None while Loop output")
dateTime = datetime.datetime.now()
print(dateTime.strftime("%H:%M:%S"))


"To Do: Task 1" 
" study the output of the code above and the output in in the while loop below, and use the links provide to answer"

" What is the while loop doing?"

" add comment to explain what you understand the 'datetime.datetime.now().strftime('%H:%M:%S')'"

" add comment to explain what you understand the 'end='"
# https://www.toppr.com/guides/python-guide/questions/what-does-end-do-in-python/

" add comment to explain what you understand the '\r' "
# https://www.w3schools.com/python/gloss_python_escape_characters.asp

" add comment to explain what you understand the 'end=' is used for"

" add comment to explain what you understand the '\r' is used for "

" What will output if you remove  , end='\r'  from the while loop"

print("while Loop output")
while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), end="\r")

    # time.sleep(1)

"Further reading on python while statements"
# https://www.w3schools.com/python/ref_keyword_while.asp
# https://www.w3schools.com/python/python_ref_keywords.asp
# https://www.w3schools.com/python/python_reference.asp