# Functions go up here...
def yes_no(question):
    valid = False
    while not valid:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"


        elif response == "no" or response == "n":
            return "no"

        else:
            print("Please answer yes / no")

# Main Routine over here...
show_instructions = yes_no("Have you played the game before? ")

print("You chose {}".format(show_instructions))
print()
having_fun = yes_no("You havin fun mate? ")
print("You said {} to having fun".format(having_fun))