"""Added 06_String_Validator to 00_MMF_base_v7
Added the import re libraries as well.
"""
# Import statements
import re

import pandas

# Functions go here


# This function splits snacks into quantity and snack name
# It has to be called before the snack (name) can be evaluated against the
# valid_snacks list
def split_order(choice):
    # Regular expressions to test and find out if an item starts with a number
    number_regex = "^[1-9]"

    # If item has a number, separate the item into two: number and item
    if re.match(number_regex, choice):
        quantity_required = int(choice[0])
        snack_name = choice[1:]

    # If item has no number, assume number required is 1
    else:
        quantity_required = 1
        snack_name = choice

    # Need to remove white space from around snack
    snack_name = snack_name.strip()
    return quantity_required, snack_name


# Function takes the question and list of valid choices as parameters
def get_choice(choice, valid_choices):
    choice_error = "Sorry, that is not a valid choice"
    for list_item in valid_choices:
        if choice in list_item:
            choice = list_item[0].title()
            return choice
    print(choice_error)


# Function to collate each other
def collate_order():
    # Valid snacks holds list of all snacks. Each item is itself a list with
    # all the acceptable input options for each snack - full name, initials and
    # abbreviations, as well as a reference number
    valid_snacks = [["popcorn", "p", "corn", "(1"],
                    ["m&ms", "mms", "m", "mm", "(2"],
                    ["pita chips", "chips", "pc", "pita", "c", "(3"],
                    ["water", "w", "(4"], ["orange juice", "oj", "(5"],
                    ["x", "exit", "(6"]]

    # Valid options for yes/no questions
    valid_yes_no = [["y", "yes"], ["n", "no"]]

    # The snack_order list records the complete order for a single user
    snack_order_list = []

    # Maximum number of any snack item which can be ordered
    max_number_of_snacks = 4

    # Assumption that every user will want to order snacks
    getting_snacks = True
    while getting_snacks:
        # Firstly, find out whether the user wants to order snacks
        snacks_required = ""
        while snacks_required != "N" and snacks_required != "Y":
            # Response is passed to the generic string checking function with
            # the list of valid yes/no responses as parameters
            check_snacks = input("Do you want snacks? (Y/N): ").lower()
            snacks_required = get_choice(check_snacks, valid_yes_no)

        if snacks_required == "N":  # but if they don't want any snacks
            getting_snacks = False  # breaks the while loop

        else:
            # Otherwise, for each snack, the generic string checker is called
            # with the 'ask_for_snacks' question and the list of valid snacks
            # as parameters
            option = ""
            while option != "X":
                snack = input("What snack do you want - or 'x' to stop "
                              "ordering: ").lower()
                snack = split_order(snack)
                quantity = snack[0]
                if quantity > max_number_of_snacks:
                    option = None
                    print("Sorry, the maximum number you can order is 4")
                else:
                    snack = snack[1]
                    option = get_choice(snack, valid_snacks)
                    if option == "X":
                        getting_snacks = False

                    elif option is not None:  # Filters out invalid choices
                        snack_order_list.append([quantity, option])
    return snack_order_list


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

        # Get snacks
        snack_order = collate_order()

        # After the loop is broken, check for an empty list
        if len(snack_order) > 0:
            # If there is something in the list, print each item
            print("\nThis is a summary of your order:")
            for item in snack_order:
                print(f"\t{item[0]} {item[1]}")
        else:  # Otherwise, print this
            print("No snacks were ordered")

        # Check to ensure there are still tickets left
        max_tickets_checker(MAX_TICKETS, ticket_count)

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
