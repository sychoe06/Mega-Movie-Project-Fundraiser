"""This version checks to see if there is only ONE ticket left and, if so,
produces a more appropriately worded print statement.
The layout of the code has been spaced out to improve readability.
"""

# Initialise loop so that it runs at least once
name = ""
count = 0
MAX_TICKETS = 5
print(f"You have {MAX_TICKETS} tickets that have not been sold yet\n")

while name != "Xxx" and count != MAX_TICKETS:
    # Get details
    name = input("What's your name? ").title()
    count += 1
    num_of_seats = MAX_TICKETS - count
    if name != "Xxx" and count == MAX_TICKETS:
        print("\nYou have sold all the available tickets")
    elif MAX_TICKETS - count == 1:
        # Warns user there is only one seat left
        print(f"*** You have ONLY ONE seat left! ***\n")
    elif name != "Xxx" and count != MAX_TICKETS:
        print(f"You have {num_of_seats} seats left\n")
    else:
        count -= 1  # Don't want to include escape in the count
        num_of_seats = MAX_TICKETS - count
        print(f"\nYou have sold {count} tickets.\n"
              f"There are still {num_of_seats} available")
