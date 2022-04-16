"""Based on 00_MMF_base_v15

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
    valid_snacks = [["popcorn", "p", "pop", "corn", "(1"],
                    ["m&ms", "mms", "m", "mm", "(2"],
                    ["pita chips", "chips", "pc", "pita", "c", "(3"],
                    ["water", "h20", "w", "(4"],
                    ["orange juice", "o", "oj", "juice", "(5"],
                    ["x", "exit", "(6"]]

    # The snack_order list records the complete order for a single user
    snack_order_list = []

    # Maximum number of any snack item which can be ordered
    max_number_of_snacks = 4

    option = ""
    while option != "X":
        snack = input("What snack do you want - qty then item"
                      "\n e.g. '2 popcorn' OR 'x' to stop ordering: ").lower()
        snack = split_order(snack)
        quantity = snack[0]

        if quantity > max_number_of_snacks:
            option = None
            print("Sorry, the maximum number you can order is 4")
        else:
            snack = snack[1]
            option = get_choice(snack, valid_snacks)
            if option == "X":
                break
            elif option is not None:  # Filters out invalid choices
                snack_order_list.append([quantity, option])
    return snack_order_list


# Calculate the ticket price (based on given age)
def calc_ticket_price(ages):
    # Ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if ages in child_age:
        ticket = child_price
    elif ages in standard_age:
        ticket = standard_price
    else:
        ticket = retired_price
    return ticket


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


# Check that the ticket name is not blank
def not_blank(question):
    valid = ""
    while not valid:
        response = input(question).title()

        # If the name is blank, it shows this error message
        if not response.isalpha():  # Ensures input contains at least 1 letter
            print("You can't include digits or leave this blank...\n")
        else:
            return response  # But if name is not blank, program continues


# Checks for valid age to purchase a ticket
def valid_age_checker(minimum, maximum):
    valid_age = number_checker(f"Please enter {name}'s age: ")
    if valid_age < minimum:  # if age is younger than 12
        # then ticket isn't sold
        return None
    else:
        while not valid_age <= maximum:  # while age is not between 12 and 110
            valid_age = number_checker(f"\nAt {valid_age} {name} is very old. "
                                       f"Please re-enter {name}'s age: ")
            if valid_age < minimum:  # if re-entered age is younger than 12
                # then ticket isn't sold
                return None
        return valid_age


def check_valid_payment_method():
    ask_payment_method = input("How do you want to pay: ").lower()
    valid_payment_method = [["credit card", "card", "credit", "cc", "cr", "1"],
                            ["eftpos", "eft", "pos", "ep", "e", "2"], ["cash",
                            "ca", "money", "notes", "coins", "c", "3"]]
    payment_methods = get_choice(ask_payment_method, valid_payment_method)
    return payment_methods


# Checks number of tickets that are sold and how many are left
def ticket_counting(tickets_sold, maximum):
    if tickets_sold < maximum:
        # Making sure it reads OK when only one ticket sold
        if tickets_sold > 1:
            print(f"{tickets_sold} tickets have now been sold")
        # Making sure it reads OK when 0 tickets have sold
        elif tickets_sold == 0:
            print("No tickets have been sold")
        else:
            print("1 ticket has now been sold")

        # Print how many tickets are still available
        if maximum - tickets_sold > 1:
            print(f"{maximum - tickets_sold} tickets are still available")
        else:
            # Making sure it reads OK when only one ticket left
            print("1 ticket is still available")
    else:
        print("!!!!! All available tickets have now been sold !!!!!")


# Checks how many tickets are left that can be sold
def max_tickets_checker(maximum, sold):
    if maximum - sold > 1:
        print(f"\nThere are {maximum - sold} tickets left\n")
    elif maximum - sold == 1:
        # Warns user there is only one ticket left
        print(f"\n*** There is ONLY ONE ticket left! ***\n")
    else:
        print(f"\nALL TICKETS HAVE BEEN SOLD!!\n")


# Currency formatting function
def currency(number):
    return f"${number:,.2f}"


# Function containing instructions
def show_instructions(valid_responses):
    instructions = ""
    while not instructions:
        instructions = not_blank("Would you like to read the "
                                 "instructions?: ").lower()
        instructions = (get_choice(instructions, valid_responses))

    if instructions == "Y":
        print()
        print("-" * 60)
        print("\n\t**** Mega Movie Fundraiser Instructions ****\n"
              "\nYou will be shown how many tickets are still available\n"
              "for sale and asked for the first ticket-purchaser's name.\n"
              "You will then be asked to input the ticket-purchaser's age.\n"
              "\nThis is because:\n"
              "\t- the minimum age for entry is 12; and\n"
              "\t- there is a standard price for adults; but\n"
              "\t- different prices for students and retired people.\n"
              "\nThe program will then ask you for the snacks required\n"
              "and once these are entered you will then need to provide a\n"
              "valid method of payment.\n"
              "\nThis process keeps repeating until either all tickets are\n"
              "sold or you choose to exit the program.\n"
              "\nOn exit, a summary of sales and profits will be printed to\n"
              "the screen. Full details of all sales and profits are also\n"
              "output to .csv files. These can be found in the same\n"
              "directory in which the program is stored.\n")
        print("-" * 60)
    print("\nProgram launches...\n")


# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data
all_names = []
all_tickets = []

# Creates separate list for each snack type
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

# Put the separate lists above into a master list
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Store surcharge multiplier
surcharge_mult_list = []

# Lists to store summary data
# Heading order matches the lists in the 'snack_lists' master list above
summary_headings = ["Popcorn", "M&Ms", "Pita Chips", "Water", "Orange Juice",
                    "Snack Profit", "Ticket Profit", "Total Profit"]

# Empty list to hold the data for above summary
summary_data = []

# Data frame Dictionary
movie_data_dict = {
    "Name": all_names,
    "Ticket": all_tickets,
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&Ms": mms,
    "Orange Juice": orange_juice,
    "Surcharge Multiplier": surcharge_mult_list
}

# Dictionary to hold summary information
summary_data_dict = {
    "Item": summary_headings,
    "Amount": summary_data
}

# Cost of each snack
price_dict = {
    "Popcorn": 2.5,
    "Water": 2,
    "Pita Chips": 4.5,
    "M&Ms": 3,
    "Orange Juice": 3.25
}
SNACK_PROFIT_MARGIN = .2
SURCHARGE_RATE = .05
MAX_TICKETS = 150
WHOLE_SALE_TICKET = 5
MIN_AGE = 12
MAX_AGE = 110
name = ""
ticket_count = 0
ticket_profit = 0
ticket_price = 0
surcharge_multiplier = 0
total = 0

# Ask user if they have used the program before and
# show instructions if necessary
print("*** Welcome to Mega Movie ***")

# Valid options for any yes/no questions
valid_yes_no = [["y", "yes"], ["n", "no"]]
show_instructions(valid_yes_no)

# Shows users how many max tickets there are at the start before selling
print(f"There are {MAX_TICKETS} tickets that have not been sold yet\n")

# Loop to get ticket details
# Initialise loop so that is runs at least once

while name != "X" and ticket_count != MAX_TICKETS:
    # Get details
    # Get name (can't be blank)
    name = not_blank("Enter ticket-holder's name: ").title()
    if name == "X":
        break  # breaks out of loop. so escape is not counted as a ticket sale
    else:
        # Check for a valid age (between 12 and 110)
        age = valid_age_checker(MIN_AGE, MAX_AGE)
        if age is None:
            print(f"Sorry, {name} is too young for this movie")

        else:
            ticket_count += 1  # added to number of tickets sold

            # Calculate ticket price
            ticket_price = calc_ticket_price(age)
            print(f"For {name} the price is ${ticket_price:.2f}")

            # Add name and ticket price to lists
            all_names.append(name)
            all_tickets.append(ticket_price)
            ticket_profit += (ticket_price - WHOLE_SALE_TICKET)

            # Get snacks
            snack_order = collate_order()

            # Assume no snacks have been bought
            for item in snack_lists:
                item.append(0)  # add 0 as the amount for each item

            # Print snack_order
            for item in snack_order:  # item has only 2 parts, number and snack
                if len(item) > 0:  # Checking to eliminate any blank orders
                    to_find = item[1]  # Gets snack name for the item ordered
                    amount = item[0]  # and sets 'amount' to number ordered
                    # Matches the snack name to the movie_data_dict
                    add_list = movie_data_dict[to_find]
                    # Appends the number ordered to the end of the dictionary
                    # list of quantities ordered eg if the most recent quantity
                    # is 3 it would be added to the end of
                    # this list: [2, 5, 0, 1, 3]
                    add_list[-1] = amount

            # After the loop is broken, check for an empty list
            if len(snack_order) > 0:
                # If there is something in the list, print each item
                print("\nThis is a summary of your order:")
                for item in snack_order:
                    print(f"\t{item[0]} {item[1]}")
                print()  # added space
            else:  # Otherwise, print this
                print("No snacks were ordered")

            # Get payment method (and work out surcharge as necessary)
            payment_method = check_valid_payment_method()
            while not payment_method:
                payment_method = check_valid_payment_method()

            if payment_method == "Credit Card":
                surcharge_multiplier = SURCHARGE_RATE

            else:
                surcharge_multiplier = 0

            surcharge_mult_list.append(surcharge_multiplier)

        # Check to ensure there are still tickets left
        max_tickets_checker(MAX_TICKETS, ticket_count)

# End of tickets/snacks/payment loop

# Print details
movie_frame = pandas.DataFrame(movie_data_dict)
movie_frame = movie_frame.set_index("Name")  # Changes the index to reference

# Calculate the collective price of snacks ordered
movie_frame["Snack Cost"] = \
    movie_frame["Popcorn"] * price_dict["Popcorn"] + \
    movie_frame["Water"] * price_dict["Water"] + \
    movie_frame["Pita Chips"] * price_dict["Pita Chips"] + \
    movie_frame["M&Ms"] * price_dict["M&Ms"] + \
    movie_frame["Orange Juice"] * price_dict["Orange Juice"]

movie_frame["Sub Total"] = movie_frame["Snack Cost"] + movie_frame["Ticket"]

movie_frame["Surcharge"] = \
    movie_frame["Sub Total"] * movie_frame["Surcharge Multiplier"]

movie_frame["Total"] = movie_frame["Sub Total"] + movie_frame["Surcharge"]

# Shorten column names
movie_frame = movie_frame.rename(columns={"Orange Juice": "OJ",
                                          "Pita Chips": "Chips",
                                          "Surcharge Multiplier": "SM"})

# Set up summary data frame
# Populate snack items from the master snack_lists
for item in snack_lists:
    # Sum items in each snack list
    summary_data.append(sum(item))

# Get snack profit
# Get snack total from panda
snack_total = movie_frame["Snack Cost"].sum()
snack_profit = snack_total * SNACK_PROFIT_MARGIN

# Work out total profit and add to list
total_profit = snack_profit + ticket_profit
# Format profit figures and add to summary list
currency_amounts = [snack_profit, ticket_profit, total_profit]
for amount in currency_amounts:
    amount = currency(amount)
    summary_data.append(amount)

# Creates the summary frame
summary_frame = pandas.DataFrame(summary_data_dict)
summary_frame = summary_frame.set_index("Item")

# Force all columns to be printed
pandas.set_option("display.max_columns", 999)

# **** Pre Printing / Export ****
# Format currency values so they have $'s
# Ticket details formatting (using currency function)
currency_amounts = ["Ticket", "Snack Cost", "Sub Total", "Surcharge", "Total"]
for amount in currency_amounts:
    movie_frame[amount] = movie_frame[amount].apply(currency)  # this is a call
    # to the currency() function above

# Write each frame to separate csv files
movie_frame.to_csv("ticket_details.csv")
summary_frame.to_csv("snack_summary.csv")

print("-" * 60)

# Printing the abbreviated table
print("*** Ticket/Snack information ***")
# Refers to an export file - functionality yet to be developed
print("Note: for full details please see the excel file called "
      "snack_summary.csv; and ticket_details.csv\n")
print(movie_frame[["Ticket", "Snack Cost", "Sub Total", "Surcharge", "Total"]])

# Printing the summary frame
print("\n*** Snack/Profit Summary ***\n")
print(summary_frame)
print()

# Remaining tickets
ticket_counting(ticket_count, MAX_TICKETS)

print("-" * 60)

# Output data to text file
