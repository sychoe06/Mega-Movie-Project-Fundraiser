def not_blank(question, error_message):
    valid = ""
    while not valid:
        response = input(question)
        if not response:
            print(error_message)
        else:
            return response


# ******** Main Routine ********
name = not_blank("What is your name? ", "You cannot leave this blank...")
