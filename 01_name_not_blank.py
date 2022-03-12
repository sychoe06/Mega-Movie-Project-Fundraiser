def not_blank(question):
    valid = ""
    while valid == "":
        response = input(question)
        if response <= " ":
            print("You cannot leave this blank...")
        else:
            return response


# ******** Main Routine ********
name = not_blank("What is your name? ")
