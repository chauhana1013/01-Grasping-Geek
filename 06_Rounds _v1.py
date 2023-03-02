balance = 5

rounds_played = 0

play_again = input("Hey Bro, gotta press < ENTER > to continue...").lower()
while play_again == "":
    rounds_played += 1

    print()
    print("*** Round #{} ***".format(rounds_played))
    balance -= 1
    print("Balance: ", balance)
    print()

    if balance < 1:
        play_again = "xxx"
        print("Sorry bro, you ran out of money")

    else:
        play_again = input("Press < ENTER > to play again bro or type in 'xxx' to quit  ")

print()
print("Final Balance", balance)