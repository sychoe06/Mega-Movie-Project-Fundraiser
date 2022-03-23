"""Calculate price based on age
This function will be used in conjunction with others to check that the age
is between 12 and 110
"""


def calc_ticket_price(age):
    if age < 16:
        return CHILD_PRICE
    elif age >= 65:
        return RETIRED_PRICE
    else:
        return STANDARD_PRICE


def calc_profit(ticket):
    profit = ticket - WHOLE_SALE_TICKET
    return profit


# Main routine
CHILD_PRICE = 7.5
STANDARD_PRICE = 10.5
RETIRED_PRICE = 6.5
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
