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
            print()


def show_instructions():
    statement_generator("Instructions", "~")
    print()
    statement_generator("Pick an amount from $1.00 to $10.00", "~")
    print()
    print("Then by pressing <Enter>, the game will begin "
          "and I will generate either a Horse, Zebra, Donkey, or Unicorn")
    print()
    statement_generator("The Donkey Token  --->  -$1.00", "+")
    print()
    statement_generator("The Horse Token  --->  -$0.50", "+")
    print()
    statement_generator("The Zebra Token  --->  -$0.50", "+")
    print()
    statement_generator("The Unicorn Token  --->  +$4.00", "+")
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
                print()
        except ValueError:
            print(error)
            print()


def statement_generator(statement, decoration):
    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""


# Main Routine over here...
print()
statement_generator("Welcome to the Lucky Unicorn Game", "*")
print()


played_before = yes_no("Hey there, I am Uriah, The Host of the Lucky Unicorn Game, "
                       "have you ever played this game before? ")
print()

if played_before == "no":
    show_instructions()
    print()

# Ask user how much they want to play with...
how_much = num_check("How much would you like to play with? ", 0, 10)
balance = how_much

rounds_played = 0

play_again = input("Hey Bro, once you are ready just press < ENTER > to continue...").lower()
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
        chosen = "UNICORN"
        prize_decoration = "!"
        balance += 4

    # if the random # is between 6 and 36
    # user gets a donkey (subtract $1 from balance)
    elif 6 <= chosen_num <= 36:
        chosen = "DONKEY"
        prize_decoration = ""
        balance -= 1

    # The token is either a horse or a zebra...
    # in both cases, subtract $0.50 from the balance
    else:
        # If the number is even, set the chosen
        # item to a horse
        if chosen_num % 2 == 0:
            chosen = "HORSE"
            prize_decoration = "+"

        # Otherwise set it to a zebra
        else:
            chosen = "ZEBRA"
            prize_decoration = "+"
        balance -= 0.5

    outcome = f"YOU GOT A {chosen}, YOUR BALANCE IS ${balance:.2f}"

    statement_generator(outcome, prize_decoration)

    if balance < 1:
        play_again = "xxx"
        print("Sorry bro, you ran out of money")

    else:
        play_again = input("Press < ENTER > to play again bro or type in 'xxx' to quit  ")


print()
statement_generator("Results", "=")
print(f"Final Balance ${balance}")
print()
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
print("<|THANK YOU JOINING ME IN THE LUCKY UNICORN GAME, GOODBYE FOR NOW|>")
print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
