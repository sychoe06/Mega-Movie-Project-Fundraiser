"""Added 04_calculate_ticket_price_v4.py to original v5 of this base code
Calculates both ticket price and profit and prints it out for user

Have changed the variable 'count' to 'ticket_count' and made the formatting
and language in the print statements easier to understand.

Also edited and modified line 121 to line 135 so that it can read better when
only 1 or zero tickets are sold or when there is 1 ticket left.
"""
# Import statements

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


# Calculate the profit from selling a ticket
def calc_profit(ticket):
    profit = ticket - WHOLE_SALE_TICKET
    return profit

# ******** Main Routine ********

# Set up dictionaries / lists needed to hold data

# Ask user if they have used the program before and
# show instructions if necessary


# Loop to get ticket details
MAX_TICKETS = 5
WHOLE_SALE_TICKET = 5
name = ""
ticket_count = 0
total = 0

print(f"There are {MAX_TICKETS} tickets that have not been sold yet\n")

while name != "Xxx" and ticket_count != MAX_TICKETS:
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
                # Calculate ticket price
                price_ticket = calc_ticket_price(age)
                print(f"For {name} the price is ${price_ticket:.2f}")
                ticket_profit = calc_profit(float(price_ticket))
                total += ticket_profit

                ticket_count += 1
                num_of_tickets = MAX_TICKETS - ticket_count
                if MAX_TICKETS - ticket_count == 1:
                    # Warns user there is only one ticket left
                    print(f"\n*** There is ONLY ONE ticket left! ***\n")
                elif name != "Xxx" and ticket_count != MAX_TICKETS:
                    print(f"\nThere are {num_of_tickets} tickets left\n")

    # Get age (between 12 and 130)

    # Loop to ask for snacks

    # Calculate snack price

    # Ask for payment method (and apply surcharge if necessary)


# Calculate total sales and profit
print()
print("-" * 40)
num_of_tickets = MAX_TICKETS - ticket_count
if ticket_count < MAX_TICKETS:
    if ticket_count > 1:  # Making sure it reads OK when only one ticket sold
        print(f"{ticket_count} tickets have now been sold")
    elif ticket_count == 0:  # Making sure it reads OK when 0 tickets have sold
        print("No tickets have been sold")
    else:
        print("1 ticket has now been sold")
    if num_of_tickets > 1:
        print(f"{num_of_tickets} tickets are still available")
    else:
        # Making sure it reads OK when only one ticket left
        print("1 ticket is still available")
else:
    print("!!!!! All available tickets have now been sold !!!!!")

# Print total profit
print(f"\nTotal Profit: ${total:.2f}")
print("-" * 40)


# Output data to text file
