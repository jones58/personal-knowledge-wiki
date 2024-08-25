"To Do: Task1: Modify the code in userName function below to use parameter and arguments"

def userName(pFullname, pAddress,pInterest):  # define a subrouitine called userName
    # return f"my name is {pFullname}, my address is {pAddress} and my interest is {pInterest}"
    return pFullname,pAddress,pInterest

    # print()


fullName = input("Enter your name: ")
address = input("Enter your address: ")
interest = input("Any interest? ")

print(userName(fullName,address,interest))

myUserData = userName(fullName,address,interest)

print(myUserData[0])
print(myUserData[1])
print(myUserData[2])
print(f"My name is {myUserData[0]} , I live at {myUserData[1]} and my interest is {myUserData[2]}")