import random

weeks = ["wk1", "wk2", "wk3", "wk4", "wk5", "wk6", "wk7", "wk8", "wk9", "wk10", "wk11", "wk12"]
aWeek = random.choice(weeks)
print(aWeek)
match aWeek:
    case "wk1":
        print("Welcome to SDLC.")
    case "wk2":
        print("Welcome HTML.")
    case "wk3":
        print("Welcome to CSS.")
    case "wk4":
        print("Still CSS week.")
    case "wk5":
        print("Welcome to JavaScript.")
    case "wk6":
        print("Welcome JavaScript project.")
    case "wk7":
        print("Welcome to Database.")
    case "wk8":
        print("Still database week.")
    case "wk9":
        print("Welcome Python .")
    case "wk10":
        print("Still Python week.")
    case "wk11":
        print("Welcome Python Project week.")
    case "wk12":
        cohortName = input("Enter cohort name: ")
        if cohortName == "Man":
            print("Microsoft Azure week.")
        else:
            print("Portfolio week.")
    # In the last case block, we defined case _, where the variable 
    # name _ acts as a wildcard and it will never fail to match.
    # If no case matches in the upper code then the last case block is executed.
    case _:
        print("Matches anything.")

        # https://geekpython.in/match-case-in-python