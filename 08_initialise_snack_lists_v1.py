"""Initialise snack lists - this is a completely new component - initially
just for testing.
Prints the dictionary with all quantities ordered in the test data list.
"""

names = ["Rangi", "Manaia", "Talia", "Arihi", "Fetu"]

# Creates separate list for each snack type
popcorn = []
mms = []
pita_chips = []
water = []
orange_juice = []

# Put the separate lists above into a master list
snack_lists = [popcorn, mms, pita_chips, water, orange_juice]

# Creating the Snack dictionary with a label and then the list for content
snack_menu_dict = {
    "Popcorn": popcorn,
    "Water": water,
    "Pita Chips": pita_chips,
    "M&Ms": mms,
    "Orange Juice": orange_juice
}

# Data for testing the printing routine below
test_data = [
    [[2, "Popcorn"], [1, "Pita Chips"], [1, "Orange Juice"]],
    [[]],  # This is for Manaia's order - she ordered nothing
    [[1, "Water"]],
    [[1, "Popcorn"], [1, "Orange Juice"]],
    [[1, "M&Ms"], [1, "Pita Chips"], [3, "Orange Juice"]]
]

count = 0  # Need count to get the index number of each item in the snack_order
for client_order in test_data:  # Going through each order
    # Assume no snacks have been bought
    for item in snack_lists:
        item.append(0)  # add 0 as the amount for each item

    # print(snack_lists)
    # Sets snack_order to the [count vale of index] item in test data
    snack_order = test_data[count]
    count += 1

    for item in snack_order:  # The item has only 2 parts - number and snack
        if len(item) > 0:  # Checking to eliminate any blank orders
            to_find = item[1]  # Gets the snack name for the item ordered
            amount = item[0]  # and sets 'amount' to number ordered
            # Matches the snack name to the snack_menu_dict
            add_list = snack_menu_dict[to_find]
            # Appends the number ordered to the end of the dictionary list of
            # quantities ordered eg if the most recent quantity is 3 it would
            # be added to the end of this list: [2, 5, 0, 1, 3]
            add_list[-1] = amount

# print(snack_lists)
# In a well formatted way
print(f"Popcorn: {snack_lists[0]}")
print(f"M&Ms: {snack_lists[1]}")
print(f"Pita Chips: {snack_lists[2]}")
print(f"Water: {snack_lists[3]}")
print(f"Orange Juice: {snack_lists[4]}")
