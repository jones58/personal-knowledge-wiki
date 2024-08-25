import random
anotherGo = "y"
score = 0
while  anotherGo != "n":
    die1 = random.randint(1,6)
    die2 = random.randint(1,6)
    print ("die 1, die 2 = ",die1, "  ", die2)
    if die1 == die2:
        anotherGo = 'n'
        score = 0
        print ("Score = ", score) 
    else:
        score = score + die1 + die2
        print ("Score = ", score)
        anotherGo = input ("Another go? (y or n): ")
print ("Final Score = ", score)

#Holds the screen until ENTER pressed to read results if using windows console
input("\nPress ENTER to exit program")
