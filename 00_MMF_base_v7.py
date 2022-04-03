"""Moved the check of sales against maximum tickets into its own function
Added lists to hold ticket holder's name and the price paid for their ticket
Added a dictionary to get data from these 2 new lists
Added code to append name and ticket price to the new lists (line 140 and 141)
Added the import re and import pandas libraries (installing pandas package if
necessary)
Modified the else statement (line 125-144) under 'while name != "Xxx" and
ticket_count != MAX_TICKETS:' to improve the flow and readability.
Added functions to check how many tickets are available and valid ages,
'max_tickets_checker(maximum, sold)' and 'valid_age_checker(minimum, maximum)'
Replaced the "num_of_tickets" variable with "MAX_TICKETS - ticket_count"
because it is the same thing and no need to make it a whole new variable.
Removed the 'calc_profit(ticket)' function and replaced to something more
simple 'profit += price_ticket - WHOLE_SALE_TICKET' so that it takes less lines
Added the print details (movie_frame: line 176 and 177) which uses the pandas
library to create a printable DataFrame based on the dictionary
"""
# Import statements
import re

import pandas

# Functions go here


# Check that the ticket name is not blank
def not_blank(question):
    while True:
        response = input(question).title()
        if not response.isalpha():  # Ensures input contains at least 1 letter
            print("You cannot leave this blank...\n")  # Error if not
        else:
            return response  # Otherwise, return the input


# Check for valid integer (e.g. for age)
def number_checker(question):
    number = ""
    while not number:
        try:
            number = int(input(question))
            return number
        except ValueError:
            print("\nPlease enter an integer (i.e. a whole number"
                  "with no decimals)")


# Calculate the ticket price (based on given age)
def calc_ticket_price(ages):
    # Ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if ages in child_age:
        ticket_price = child_price
    elif ages in standard_age:
        ticket_price = standard_price
    else:
        ticket_price = retired_price
    return ticket_price


# Checks how many tickets are left that can be sold
def max_tickets_checker(maximum, sold):
    if maximum - sold > 1:
        print(f"\nThere are {maximum - sold} tickets left\n")
    else:
        # Warns user there is only one ticket left
        print(f"\n*** There is ONLY ONE ticket left! ***\n")


# Checks for valid age to purchase a ticket
def valid_age_checker(minimum, maximum):
    age_ = number_checker(f"Please enter {name}'s age: ")
    if age_ < minimum:  # if age is younger than 12
        # then ticket isn't sold
        return None
    else:
        while not age_ <= maximum:  # while age is not between 12 and 110
            age_ = number_checker(f"\nAt {age_} {name} is very old. "
                                  f"Please re-enter {name}'s age: ")
            if age_ < minimum:  # if re-entered age is younger than 12
                # then ticket isn't sold
                return None
        return age_


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data
all_names = []
all_tickets = []

# Data frame Dictionary
movie_data_dict = {
    'Name': all_names,
    'Ticket': all_tickets
}

# Ask user if they have used the program before and
# show instructions if necessary

MAX_TICKETS = 5
WHOLE_SALE_TICKET = 5
MIN_AGE = 12
MAX_AGE = 110
name = ""
ticket_count = 0
total = 0
profit = 0

print(f"There are {MAX_TICKETS} tickets that have not been sold yet\n")

# Loop to get ticket details
while name != "Xxx" and ticket_count != MAX_TICKETS:
    # Get details
    # Get name
    name = not_blank("Enter ticket-holder's name: ")  # Name can't be blank
    if name == "Xxx":
        break  # breaks out of loop. so escape is not counted as a ticket sale
    else:
        # Check for a valid age (between 12 and 110)
        age = valid_age_checker(MIN_AGE, MAX_AGE)
        if age is None:
            print(f"Sorry, {name} is too young for this movie")

        else:
            ticket_count += 1  # added to number of tickets sold

            # Calculate ticket price
            price_ticket = calc_ticket_price(age)
            print(f"For {name} the price is ${price_ticket:.2f}")
            profit += price_ticket - WHOLE_SALE_TICKET

            # Add name and ticket price to lists
            all_names.append(name)
            all_tickets.append(price_ticket)

        # Check to ensure there are still tickets left
        max_tickets_checker(MAX_TICKETS, ticket_count)

        # Get snacks

        # Get payment method (and work out surcharge as necessary)

    # End of tickets/snacks/payment loop

# Calculate total sales and profit
print()
print("-" * 40)
if ticket_count < MAX_TICKETS:
    # Print number of tickets that have been sold
    if ticket_count > 1:  # Making sure it reads OK when only one ticket sold
        print(f"{ticket_count} tickets have now been sold")
    elif ticket_count == 0:  # Making sure it reads OK when 0 tickets have sold
        print("No tickets have been sold")
    else:
        print("1 ticket has now been sold")

    # Print how many tickets are still available
    if MAX_TICKETS - ticket_count > 1:
        print(f"{MAX_TICKETS - ticket_count} tickets are still available\n")
    else:
        # Making sure it reads OK when only one ticket left
        print("1 ticket is still available\n")
else:
    print("!!!!! All available tickets have now been sold !!!!!\n")

# Print details
if ticket_count != 0:  # If no tickets have been sold...
    # Then no need to print to print details of name and ticket price
    movie_frame = pandas.DataFrame(movie_data_dict)
    print(movie_frame)
print(f"\nTotal Ticket Profit: ${profit:.2f}")

print("-" * 40)

# Loop to ask for snacks

# Output data to text file
