"""Calculate price based on age - version 2
Added CHILD_AGE, RETIRED_AGE AND STANDARD AGE as constants because I thought
it would be better to use a range and constants
"""


def calc_ticket_price(age):
    CHILD_AGE = range(12, 16)
    STANDARD_AGE = range(16, 65)
    RETIRED_AGE = range(65, 111)

    CHILD_PRICE = 7.5
    STANDARD_PRICE = 10.5
    RETIRED_PRICE = 6.5

    if age in CHILD_AGE:
        return CHILD_PRICE
    elif age in STANDARD_AGE:
        return STANDARD_PRICE
    else:
        return RETIRED_PRICE


def calc_profit(ticket):
    WHOLE_SALE_TICKET = 5
    profit = ticket - WHOLE_SALE_TICKET
    return profit


# Main routine
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
