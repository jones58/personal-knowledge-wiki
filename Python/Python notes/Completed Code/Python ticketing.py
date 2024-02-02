from datetime import date

# Display welcome message and ticket pricing information
print("Welcome to the adventure Bootcamp")
print("*********************************")
def ticketPrices():
    print(" Ticket Prices\n**************\nAdult: £20\nChild: £12\nSenior citizen: £11")
# # call the ticketPrices subroutine
# ticketPrices()


# Ask for booking/ticket details and lead booker

#lead booker
def lead_booker():
    bookerName = input("Enter your name: ")
    return bookerName


def valid_num():
    invalidNum = True # create a boolean datatype which is set to true
    # repeat 
    while invalidNum: # same as while True
        try:
            number = int(input()) # sk user for integer datatype(number)
            invalidNum = False # re-assign the boolean value to for invalid to false
        except ValueError:
            print("Please enter a number: ")
    return number

# callculate tickets 
def calculate_total(pCTotal, pATotal, pStotal):
    #includes the child cost * number of child tickets
    total_cost = pCTotal * 12
    print(total_cost)
    #includes the adult cost * number of adult tickets+
    total_cost = total_cost + pATotal * 20
    print(total_cost)
    #includes the senior cost * number of senior tickets
    total_cost = total_cost + pStotal * 11
    print(f"The total cost is {total_cost}")
    return total_cost


# issue tickets and ask for payment 

def collect_tickets(total_cost):
    print("The total cost is", total_cost)
    print("Ticket machine only accepts £10s and £20s notes ")
    amount_paid = 0 # create amount_paid variable and assign it with an ineger valeu 0

    while total_cost > amount_paid:
        print(type(total_cost))
        enter_amount = valid_num()
        if enter_amount == 10:
            amount_paid = amount_paid + 10
        elif enter_amount == 20:
            amount_paid = amount_paid + 20
        else:
            print("Ticket machine only accepts £10s and £20s notes!!! ")
    if amount_paid > total_cost:
        give_change = amount_paid - total_cost
        print("Your change is", give_change)

def issue_tickets(pCTotal, pATotal, pStotal, total_cost):
    today = date.today()
    print("Your tickets are valid on ", today)
    print("Your lead booker is ", lead_name)
    print("Your total child ticket(s) is ", pCTotal)
    print("Your total adult ticket(s) is ", pATotal)
    print("Your total senior ticket(s) is ", pStotal)
    print("Your total for all tickets is ", total_cost)

def parking_requirements():
    # ask if parking is required
    required_parking = input("Do you require parking: Enter Y or N: ").upper()
    # if the user failed to enter yes or no
    while required_parking != "Y" and required_parking  != "N":
        # repeat the question asking if parking is required 
        required_parking = input("Do you require parking: Enter Y or N: ").upper()
    return required_parking

# call the ticketPrices subroutine
ticketPrices()


print("Enter the number of child tickets? ")
# call the valid_num() function and assign it respective parameter(pCTotal, pATotal, pStotal)
pCTotal = valid_num()
print("Enter the number of Adult tickets? ")
pATotal = valid_num()
print("Enter the number of Senior tickets? ")
pStotal = valid_num()

# call the calculate_total function and assign it to total_ticketsP
# total_ticketsP = calculate_total(pCTotal, pATotal,pStotal)
total_cost = calculate_total(pCTotal, pATotal,pStotal)

# call the lead_booker function and assign lead_name
lead_name = lead_booker()


# call the lcollect_tickets
# collect_tickets(total_ticketsP)
collect_tickets(total_cost)

# call the parking_requirements function and parking_Yes_No
parking_Yes_No = parking_requirements()

# call the parking_requirements function and parking_Yes_No
# issue_tickets(pCTotal, pATotal, pStotal, total_ticketsP)
issue_tickets(pCTotal, pATotal, pStotal, total_cost)

if parking_Yes_No == "Y":
    print("You have a car pass")
print("Enjoy your adventures")
