def not_blank(question):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print("You cannot leave this blank...")
        else:
            return response


# ******** Main Routine ********
name = not_blank("What is your name? ")
