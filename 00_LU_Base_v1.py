import random


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
    print("Instructions")
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
            if low < response <= high:
                return response

            # Out put an error
            else:
                print(error)

        except ValueError:
            print(error)


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine over here...
played_before = yes_no("Hey my name is Peri de Metrious, have you played the game before? ")

if played_before == "no":
    show_instructions()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)
balance = how_much

rounds_played = 0

play_again = input("Hey Bro, gotta press < ENTER > to continue...").lower()
while play_again == "":

    # increase # of rounds played
    rounds_played += 1

    print()
    rounds = ("Round #{} ".format(rounds_played))
    statement_generator(rounds, ".")
    print()
    
    chosen_num = random.randint(1, 100)

    # Adjust balance
    # of the random # is between 1 and 5,
    # user gets a unicorn (add $4 to balance)
    if 1 <= chosen_num <= 5:
        chosen = "unicorn"
        prize_decoration = "!"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "donkey"
        prize_decoration = "D"
        balance -= 1

    # The token is either a horse or a zebra..
    # in both cases, subtract $0.50 from the balance
    else:
        # If the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "horse"
            prize_decoration = "H"

        # Otherwise set it to a zebra
        else:
            chosen = "zebra"
            prize_decoration = "Z"
        balance -= 0.5

    outcome = f"You got a {chosen}, your balance is ${balance:.2f}"

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry bro, you ran out of money")

    else:
        play_again = input("Press < ENTER > to play again bro or type in 'xxx' to quit  ")


print()
statement_generator("Results", "=")
print("Final Balance", balance)