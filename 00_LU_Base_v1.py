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

def num_check(question, low, high):



    error = "Hey man, choose a whole number between 1 and 10"

    valid = False
    while not valid:

        try:
            # Ask the question
            response = int(input(question))

            # If the amount is too low / too high give
            if low < response <= high :
                return response

            # Out put an error
            else:
                print(error)

        except ValueError:
            print(error)


# Main Routine over here...
played_before = yes_no("Hey my name is Peri de Metrious, have you played the game before? ")

if played_before == "no":
    show_instructions()

print("Program Continues")




# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)

print("You will be spending ${}".format(how_much))