"""Calculate price based on age - version 2
Don't need "RETIRED_AGE" constant because it can be inferred.
Changed constants in function to ordinary variables
"""


def calc_ticket_price(age):
    # Ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        return child_price
    elif age in standard_age:
        return standard_price
    else:
        return retired_price


def calc_profit(ticket):
    profit = ticket - WHOLE_SALE_TICKET
    return profit


# Main routine
WHOLE_SALE_TICKET = 5
name = ""
total = 0
# Used a while loop for testing purposes
while name != "Xxx":
    # Temporary input statements - during development
    name = input("What is your name? ").title()
    if name == "Xxx":
        break
    else:
        ticket_buyer_age = int(input("How old are you? "))
        ticket_price = calc_ticket_price(float(ticket_buyer_age))
        print(f"Ticket price: ${ticket_price:.2f}\n")
        ticket_profit = calc_profit(float(ticket_price))
        total += ticket_profit
print(f"Total: ${total:.2f}")
