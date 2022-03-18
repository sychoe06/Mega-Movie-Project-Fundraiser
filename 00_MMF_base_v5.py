"""Edited the get name and valid age coding so that it works properly together
So age must be between 12 and 110 for it to be counted as a ticket sale.
"""
# Import statements

# Functions go here

# Check that the ticket name is not blank
def not_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():  # Ensures input contains at least 1 letter
            print("You cannot leave this blank...")  # Error if not
        else:
            return response  # Otherwise, return the input


def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer (i.e. a whole number"
                  "with no decimals)")

# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# Loop to get ticket details
name = ""
count = 0
MAX_TICKETS = 5
print(f"You have {MAX_TICKETS} tickets that have not been sold yet\n")

while name != "Xxx" and count != MAX_TICKETS:
    # Get name (can't be blank)
    name = not_blank("Enter ticket-holder's name: ")
    if name == "Xxx":
        break  # breaks out of loop. so escape is not counted as a ticket sale
    else:
        # Main routine
        # Check for a valid age
        MINIMUM_AGE = 12
        MAXIMUM_AGE = 110
        age = number_checker(f"Please enter {name}'s age: ")
        if age < MINIMUM_AGE:
            print(f"Sorry, {name} is too young for this movie\n")
        else:
            while not age <= MAXIMUM_AGE:  # age must be between 12 and 110
                age = number_checker(f"\nAt {age} {name} is very old. "
                                     f"Please re-enter {name}'s age: ")
                if age < MINIMUM_AGE:
                    print(f"Sorry, {name} is too young for this movie\n")
                    break
            if not age < MINIMUM_AGE:  # age must not be younger than 12
                count += 1
                num_of_seats = MAX_TICKETS - count
                if MAX_TICKETS - count == 1:
                    # Warns user there is only one seat left
                    print(f"*** You have ONLY ONE seat left! ***\n")
                elif name != "Xxx" and count != MAX_TICKETS:
                    print(f"You have {num_of_seats} seats left\n")

if name != "Xxx" and count == MAX_TICKETS:
    print("\nYou have sold all the available tickets")
else:
    num_of_seats = MAX_TICKETS - count
    print(f"\nYou have sold {count} tickets.\n"
          f"There are still {num_of_seats} available")

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file
