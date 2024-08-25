#This python compare password entered with stored password 
"To Do: Predict, then Run, and then Investigate"


storedPassword = "Bootcamp"
passwordValid = False
passwordAttempt = 1

while passwordAttempt <= 3:
    password = input ("Enter user system password: ")
    if password == storedPassword:
        passwordValid = True
        break
    else:
        print ("You have enterd an incorrect password...Try again")
        passwordAttempt += 1
        
if passwordValid:
    print("You have entered a valid password. Password accepted")
else:
    print ("Login Failed")

input ("\n Press Enter to continue ")
