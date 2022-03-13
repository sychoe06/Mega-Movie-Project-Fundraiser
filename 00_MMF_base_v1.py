"""Added 01_name_not_blank_v3 to original v1 of this base code
"""
# Import statements

# Functions go here

# Check that the ticket name is not blank
def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():  # Ensures input contains at least 1 letter
            print("You cannot leave this blank...")  # Error if not
        else:
            return response  # Otherwise, return the input

# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before and
# show instructions if necessary

# Loop to get ticket details

    # Get name (can't be blank)
    name = not_blank("What is your name? ", )

    # Get age (between 12 and 130)

    # Calculate ticket price

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)

# Calculate total sales and profit

# Output data to text file
