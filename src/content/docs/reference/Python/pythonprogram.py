"""
Introduction
Create a program in python that can simulate a ticketing system for Adventure Theme Park, the python application will ask the user the list of questions below before calculating their total charge.

Your program should

Provide a welcome message
Display the entrance ticket prices
Ask how many adult tickets are required
Ask how many child tickets are required
Ask how many senior citizen tickets are required


Ask for the lead booker surname (for the ticket)

Ask if they require a parking pass for the car park

Add the total number of tickets to display the total cost

Print a ticket (display lead booker surname, tickets purchased, today’s date*)

Print a car parking pass (if requested)

Use data validation techniques to avoid runtime errors through incorrect data entry

Thank the customer for their purchase

*You will need to investigate how to add today's date to the ticket.



Entrance ticket type example

Adult			£20

Child			£12

Senior citizen		£11



Parking

Free (car pass must be displayed/printed if yes is selected)

Design

Design your program

--Think carefully about what will be needed in the main program and in each subroutine/function.

*You will need to research how to add today's date to the ticket (Hint: import datetime or date).

"""

def ticketBot():
    import datetime
    print("Welcome to Adventure Theme Park")
    print("Entrance Ticket Prices:")
    print("Adult: £20")
    print("Child: £12")
    print("Senior Citizen: £11")

    while True:
        try:
            adult_tickets = int(input("How many adult tickets are required? "))
            if adult_tickets >= 0:
                break
            else:
                print("Please enter a valid number of adult tickets.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            child_tickets = int(input("How many child tickets are required? "))
            if child_tickets >= 0:
                break
            else:
                print("Please enter a valid number of child tickets.")
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            senior_tickets = int(input("How many senior citizen tickets are required? "))
            if senior_tickets >= 0:
                break
            else:
                print("Please enter a valid number of senior citizen tickets.")
        except ValueError:
            print("Please enter a valid number.")

    lead_booker = input("Enter surname for lead booker: ")

    while True:
        parking_pass = input("Do you require a parking pass for the car park? (yes/no): ").lower()
        if parking_pass == "yes" or parking_pass == "no":
            break
        else:
            print("Please enter 'yes' or 'no'.")

    total_cost = adult_tickets * 20 + child_tickets * 12 + senior_tickets * 11
    print(
        f"Here's your ticket:\nLead booker: {lead_booker}\nAdult Tickets: {adult_tickets}\nChild Tickets: {child_tickets}\nSenior Citizen Tickets: {senior_tickets}\nTotal Cost: £{total_cost}\nDate: {datetime.date.today()}"
    )
    if parking_pass == "yes":
        print(f"Here's your car parking pass for the car park on {datetime.date.today()}")
    print("Thank you for your purchase")

if __name__ == "__main__":
    ticketBot()
