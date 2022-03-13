def not_blank(question):
    while True:
        response = input(question)
        if not response.isalpha():
            print("You cannot leave this blank...")
        else:
            return response


# ******** Main Routine ********
name = not_blank("What is your name? ", )
