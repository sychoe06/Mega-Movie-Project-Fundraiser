"""Calculate price based on age - version 2
Set up a for loop instead of while loop to run tests - according to test plan
Assumes this function will be run in conjunction with integer checking and
valid age components.
Also added "ticket_price" inside "calc_ticket_price(age)" function and added
decorations around the total price to make it stand out
"""


def calc_ticket_price(age):
    # Ages - anything over standard_age must qualify for retired price
    child_age = range(12, 16)
    standard_age = range(16, 65)

    child_price = 7.5
    standard_price = 10.5
    retired_price = 6.5

    if age in child_age:
        ticket_price = child_price
    elif age in standard_age:
        ticket_price = standard_price
    else:
        ticket_price = retired_price
    return ticket_price


def calc_profit(ticket):
    WHOLE_SALE_TICKET = 5
    profit = ticket - WHOLE_SALE_TICKET
    return profit


# Main routine
# loop for testing purposes
total = 0
test_cases = [["Rangi", 15], ["Manaia", 16], ["Talia", 64], ["Arihi", 65]]

for test in test_cases:
    test_name = test[0]
    test_age = test[1]
    price_ticket = calc_ticket_price(test_age)
    print(f"For {test_name} the price is ${price_ticket:.2f}")
    ticket_profit = calc_profit(float(price_ticket))
    total += ticket_profit

print("-" * 30)
print(f"Total: ${total:.2f}")
print("-" * 30)
