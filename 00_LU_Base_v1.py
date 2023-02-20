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

def show_instructions():
    print("********* Instructions ***********")
    print()
    print("Rules")
    print()

# Main Routine over here...
played_before = yes_no("Hey my name is Peri de Metrious, have you played the game before? ")

if played_before == "no":
    show_instructions()

print("Program Continues")




# Hey again, Peri here. I see that you're a newbie and want to find