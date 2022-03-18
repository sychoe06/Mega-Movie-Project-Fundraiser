"""Added 03_age_validator_v4 to original v3 of this base code
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


# Checks for valid integer
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
    name = not_blank("What's your name? ")
    count += 1
    num_of_seats = MAX_TICKETS - count
    if name != "Xxx":
        break
    else:
        # Main routine
        # Check for a valid age
        MINIMUM_AGE = 12
        MAXIMUM_AGE = 110
        age = number_checker("Please enter the age of the ticket-holder: ")
        if age < MINIMUM_AGE:
            print("Sorry, you are too young for this movie")
        else:
            while age <= MAXIMUM_AGE:  # age must be between 12 and 110
                age = number_checker("\nPlease enter an integer between 12 and 110: ")
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

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file
