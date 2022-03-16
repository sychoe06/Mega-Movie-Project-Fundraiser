# Start of loop

# Initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5

while name != "Xxx" and count != MAX_TICKETS:
    # Get details
    name = input("What's your name? ").title()
    count += 1
    num_of_seats = MAX_TICKETS - count
    if name != "Xxx" and count == MAX_TICKETS:
        print("You have sold all the available tickets")
    elif name != "Xxx" and count != MAX_TICKETS:
        print(f"You have {num_of_seats} seats left")
    else:
        count -= 1
        num_of_seats = MAX_TICKETS - count
        print(f"\nYou have sold {count} tickets.\n"
              f"There are still {num_of_seats} available")
