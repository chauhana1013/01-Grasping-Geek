# Functions go here
def num_check(question, low, high):



    error = "Hey man, choose a whole number between 1 and 10"

    valid = False
    while not valid:

        try:
            # Ask the question
            response = int(input("How many points you want to play with? "))

            # If the amount is too low / too high give
            if 0 < response <= 10 :
                print("You chose to play with ${}".format(response))

            # Out put an error
            else:
                print(error)

        except ValueError:
            print(error)

# Main routine go here