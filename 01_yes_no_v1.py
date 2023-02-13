# Ask the user if they have played before
played_before = input("Have you played this game before? ").lower()

# If they say yes, output 'program continues'
if played_before == "yes" or "y":
    print("program continues")

# If they say no, output 'display instructions'
elif played_before == "no" or "n":
    print("Display Instructions")

# If they say something else, the code asks them to answer in yes/no
else:
    print("Please answer yes / no")
