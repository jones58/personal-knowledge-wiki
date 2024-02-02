cardValue = "Kings"
suitOfCards = "Hearts"

"Predict, then Run, and then Investigate"
chkCardValue = input("Enter card value: ").title()

chkCardSuit = input("Enter card suit: ").title()


if cardValue == chkCardValue and suitOfCards == chkCardSuit:
    print("Winner!")
else:
    print("Try Again")


"Modify"
"To Do: Exercise"
# Modify the code above to use the "or" operator, or the "not" operator with the and operator
